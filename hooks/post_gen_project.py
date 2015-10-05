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
shutil.rmtree('sphinxdocs')

{% elif cookiecutter.docs_tool == "sphinx" %}

logger.info('Moving files for sphinx.')
shutil.move('sphinxdocs', 'docs')
shutil.rmtree('mkdocs')

{% else %}

logger.info('Removing all documentation files')
shutil.rmtree('mkdocs')
shutil.rmtree('sphinxdocs')

{% endif %}


logger.info('Removing jinja2 macros')
shutil.rmtree('macros')
