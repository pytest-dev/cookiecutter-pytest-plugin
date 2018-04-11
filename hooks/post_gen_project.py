#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')

DOC_SOURCES = 'doc_sources'
ALL_TEMP_FOLDERS = [DOC_SOURCES, 'licenses', 'macros']
DOC_TYPE_FILES_MAP = {
    'mkdocs': ['index.md', '/mkdocs.yml'],
    'sphinx': ['conf.py', 'index.rst', 'make.bat', 'Makefile']
}

def move_doc_files(which, map_=DOC_TYPE_FILES_MAP, doc_sources=DOC_SOURCES):
    root = os.getcwd()
    docs = 'docs'
    logger.info('Initializing docs for %s' % which)
    if not os.path.exists(docs):
        os.mkdir(docs)
    for item in map_[which]:
        dst, name = (root, item[1:]) if item.startswith('/') else (docs, item)
        src_path = os.path.join(doc_sources, which, name)
        dst_path = os.path.join(dst, name)
        logger.info('Moving %s to %s.' % (src_path, dst_path))
        if os.path.exists(dst_path):
            os.unlink(dst_path)
        os.rename(src_path, dst_path)


def tidy_up(temp_folders=ALL_TEMP_FOLDERS):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s" % folder)
        shutil.rmtree(folder)


if __name__ == '__main__':
    move_doc_files("{{cookiecutter.docs_tool}}")
    tidy_up()

