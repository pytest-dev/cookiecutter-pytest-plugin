# -*- coding: utf-8 -*-

import re
import random

import pytest

ZEN = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

WORDS = (word + ' ' for word in ZEN.split(' '))


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
    # outcome = yield
    # rep = outcome.get_result()

    # if random.randint(0, 100) < 30:
        # rep.outcome = 'failed'


def pytest_report_teststatus(report):
    if pytest.config.option.{{cookiecutter.plugin_name}} is False:
        return
    try:
        word = next(WORDS)
    except StopIteration:
        return report.outcome, '.', report.outcome.upper()

    if report.failed or report.skipped:
        word = re.sub(r'\S', '*', word)
    return report.outcome, word, report.outcome.upper()


def pytest_addoption(parser):
    group = parser.getgroup('{{cookiecutter.plugin_name}}')
    group.addoption(
        '--{{cookiecutter.plugin_name}}',
        action='store_true',
        default=False,
        help='Having fun with pytest at #EuroPython'
    )


def pytest_configure(config):
    if config.option.{{cookiecutter.plugin_name}}:
        config.option.verbose = -1
