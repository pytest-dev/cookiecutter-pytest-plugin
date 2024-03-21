#!/usr/bin/env python

import logging
import os
import shutil
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

ALL_TEMP_FOLDERS = ["licenses", "macros", "py_sources"]

PY_SOURCES = "py_sources"


def move_py_files(variant, save_path, save_type):
    if variant == "none" or save_path == "none":
        return

    logger.info("Initializing python for %s - %s", variant, save_type)

    py_files = glob.glob(f"{PY_SOURCES}/{save_type}/{variant}/*")

    for src_path in py_files:
        filename = os.path.basename(src_path)
        dst_path = os.path.join(save_path, filename)

        logger.info("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


if __name__ == "__main__":
    root = os.getcwd()
    variant = "{{cookiecutter.variant}}"
    module_name = "nomad_{{cookiecutter.module_name}}"
    src_path = os.path.join(root, "src", module_name)
    assert os.path.isdir(src_path), f"{src_path=} doesn't exist"
    test_path = os.path.join(root, "tests")
    assert os.path.isdir(test_path), f"{test_path=} doesn't exist"
    move_py_files(variant=variant, save_path=src_path, save_type="src")
    move_py_files(variant=variant, save_path=test_path, save_type="tests")
    remove_temp_folders(ALL_TEMP_FOLDERS)
