#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

DOCS_SOURCES = "docs_sources"
ALL_TEMP_FOLDERS = [DOCS_SOURCES, "licenses", "macros"]
DOCS_FILES_BY_TOOL = {
    "mkdocs": ["index.md", "/mkdocs.yml"],
    "sphinx": ["conf.py", "index.rst", "make.bat", "Makefile"],
}


def move_docs_files(docs_tool, docs_files, docs_sources):
    if docs_tool == "none":
        return

    root = os.getcwd()
    docs = "docs"

    logger.info("Initializing docs for %s", docs_tool)
    if not os.path.exists(docs):
        os.mkdir(docs)

    for item in docs_files[docs_tool]:
        dst, name = (root, item[1:]) if item.startswith("/") else (docs, item)
        src_path = os.path.join(docs_sources, docs_tool, name)
        dst_path = os.path.join(dst, name)

        logger.info("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)

def apply_readme_file_extension(extension):
    if extension.endswith("(.rst)"):
        extension = ".rst"
    elif extension.endswith("(.md)"):
        extension = ".md"
    else:
        logger.warning("README file extension unknown: %s", extension)
        sys.exit(1)

    readme_path = os.path.join(
        os.getcwd(),
        "README.template"
    )

    if os.path.exists(readme_path):
        new_path = os.path.join(
            os.getcwd(),
            "README" + extension
        )
        os.rename(readme_path, new_path)


if __name__ == "__main__":
    apply_readme_file_extension("{{cookiecutter.readme_format}}")
    move_docs_files("{{cookiecutter.docs_tool}}", DOCS_FILES_BY_TOOL, DOCS_SOURCES)
    remove_temp_folders(ALL_TEMP_FOLDERS)
