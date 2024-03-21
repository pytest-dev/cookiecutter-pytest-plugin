#!/usr/bin/env python

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

ALL_TEMP_FOLDERS = ["licenses", "macros"]


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
