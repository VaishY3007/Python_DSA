import pytest

def test_CMDLineArgs(request):
    arg = request.config.getoption('--test-one')
    print(f'option --test passed with {arg}')