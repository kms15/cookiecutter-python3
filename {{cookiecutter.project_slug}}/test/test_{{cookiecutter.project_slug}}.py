# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}

import {{cookiecutter.project_slug}}
import pytest


def test_foo():
    # here's an example of a simple test
    assert {{cookiecutter.project_slug}}.foo(3) == 5

    # here's how to test that an exception is raised:
    with pytest.raises(TypeError) as e:
        {{cookiecutter.project_slug}}.foo("b")
    assert str(e.value) == "unsupported operand type(s) for +: 'int' and 'str'"
