import pytest

@pytest.fixture
def someFun():
    print('\nSetup: Initialization here')
    yield
    print('\nTeardown: Cleaning Up here')

class TestClassOne:
    def testOne(self, someFun):
        print(f'\n in testOne()')
        assert True
    def testTwo(self, someFun):
            print(f'\n in testOne()')
            assert True