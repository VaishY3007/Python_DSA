import pytest

@pytest.mark.parametrize("user", ["UserA", "UserB", "UserC"])
def test_sample(user):
    print(f"User: {user}")  
    
    
    assert True

