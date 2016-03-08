# -*- coding: utf-8 -*-


def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_sth(timebox):
            assert timebox == 600
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--timebox=600',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'timebox:',
        '*--timebox=TIMEBOX*Stop test run after specified time (in seconds)',
    ])


def test_hello_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        timebox = 300
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def timebox(request):
            return int(request.config.getini('timebox'))

        def test_hello_world(timebox):
            assert timebox == 300
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_hello_world PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
