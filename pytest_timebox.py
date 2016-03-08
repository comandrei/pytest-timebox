# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    description = 'Stop test run after specified time (in seconds)'
    group = parser.getgroup('timebox')
    group.addoption(
        '--timebox',
        action='store',
        dest='timebox',
        help=description
    )

    parser.addini('timebox', description)


@pytest.fixture
def timebox(request):
    return request.config.option.timebox
