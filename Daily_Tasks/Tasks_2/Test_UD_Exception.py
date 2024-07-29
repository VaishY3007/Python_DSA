
class UDException(Exception):
    pass

def testUDExcept():
    try:
        print('\nstatement #1....')
        raise UDException('User Defined Exception')
        print('\nstatement #2....')

    except UDException as e:
        assert str(e) == 'User Defined Exception'
    else:
        assert False, 'User Defined Exception Not Raised'