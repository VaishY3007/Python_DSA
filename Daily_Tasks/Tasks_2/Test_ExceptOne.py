import pytest

def fun():
    print('\nStatement #1 in fun()...')
    raise TypeError
    print('\nStatement #2 in fun()...')
    
def testExceptionOne():
    with pytest.raises(TypeError):
        print('\nException #1 in testExceptionOne before Calling...')
        fun()
        print('\nException #2 in testExceptionOne After Calling...')