# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}


def foo(x):
    """ an example with tests in a separate file """
    return 2 + x


def bar(y):
    """an example using a doctest
    (note that you could have both external tests and doctests for the same
    function)

    Here's a simple test
    >>> bar("b")
    'ab'

    Here's an example of testing that an exception is thrown:
    >>> bar(3)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return "a" + y
