import pytest

@pytest.fixture(params=[
    ('User#1', 'Statements related to user#1'),
    ('User#2', 'Statements related to user#2'),
    ('User#3', 'Statements related to user#3'),
])
def getData(request):
    return request.param

def test_sampleOne(getData):
    user,mesg = getData
    print(f'Got from {user} --> mesg: {mesg}')
    assert True