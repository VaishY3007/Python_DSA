import pytest

@pytest.fixture
def setupTearDown():
    print('\nSetup')
    yield
    print('\nTearDown')