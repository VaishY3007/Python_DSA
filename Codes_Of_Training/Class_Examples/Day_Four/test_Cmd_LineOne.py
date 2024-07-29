import pytest



def test_CMD_LineArgs(request):
    arg = request.config.getoption('--test-one')
    print(f'option --test-one passed with {arg}')
