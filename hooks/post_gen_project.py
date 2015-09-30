#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')

import shutil
import os


{% if cookiecutter.docs_tool == "mkdocs" %}

logger.info('Moving files for mkdocs.')
os.rename('mkdocs/mkdocs.yml', 'mkdocs.yml')
shutil.move('mkdocs', 'docs')

{% endif %}
