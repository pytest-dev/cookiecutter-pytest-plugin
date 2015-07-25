# -*- coding: utf-8 -*-

def test_bar_fixture(testdir):
    testdir.tmpdir.join('test_foo.py').write('''
def test_a(bar):
    assert bar == "something"
'''
    result = testdir.runpytest('--foo=something')


def test_foo_option():
    pass
