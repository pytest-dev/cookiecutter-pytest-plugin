#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

DOCS_SOURCES = "docs_sources"
ALL_TEMP_FOLDERS = [DOCS_SOURCES, "macros"]
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


if __name__ == "__main__":
    move_docs_files("{{cookiecutter.docs_tool}}", DOCS_FILES_BY_TOOL, DOCS_SOURCES)
    remove_temp_folders(ALL_TEMP_FOLDERS)
