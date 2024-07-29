import pytest

def test_AddOne():
    assert True
@pytest.mark.xfail(True, reason='Expected Failure')
def test_Twotimes():
    assert False
    
    