#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pre_gen_project')

PLUGIN_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

plugin_name = '{{cookiecutter.plugin_name}}'

if not re.match(PLUGIN_REGEX, plugin_name):
    logger.error('Invalid value for plugin_name "{}"'.format(plugin_name))
    sys.exit(1)
