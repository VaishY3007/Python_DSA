import pytest

@pytest.fixture(scope='module')
def someFunction():
    print(f'\nSetup: for Initialization Process')
    yield
    print(f'\nTeardown: for Cleaning up resources')
    
def testTrue(someFunction):
    print('#1 My test function: performing testing')
    assert True
    
def testIsTrue(someFunction):
    print('#2 My test function: performing testing')
    assert True