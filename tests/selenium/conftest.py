import pytest


@pytest.fixture(scope='session')
def base_url(base_url, request):
    return base_url or request.getfixturevalue("live_server").url


@pytest.fixture
def capabilities(request, capabilities):
    driver = request.config.getoption('driver')
    if capabilities.get('browserName', driver).lower() == 'firefox':
        capabilities['marionette'] = True
    return capabilities


@pytest.fixture(scope='session')
def session_capabilities(pytestconfig, session_capabilities):
    if pytestconfig.getoption('driver') == 'SauceLabs':
        session_capabilities.setdefault('tags', []).append('treeherder')
    return session_capabilities


@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium
