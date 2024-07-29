import pytest

@pytest.fixture
def giveSomeData():
    return 'Ten'

def testValidData(giveSomeData):
    with pytest.raises(ValueError):
        var = int(giveSomeData)
        assert var == 10
        

    