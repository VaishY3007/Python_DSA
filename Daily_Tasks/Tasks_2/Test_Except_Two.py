import pytest

class ExceptionGroup(Exception):
    def __init__(self, message, exceptions):
        super().__init__(message)
        self.exceptions = exceptions

def fun():
    print('\nStatement #1 in fun()...')
    raise ExceptionGroup(
        "MY ERROR MESSAGE",
        [RuntimeError(),
         TypeError(),]
    )
    print('\nStatement #2 in fun()...')
    
def testExceptionOne():
    with pytest.raises(ExceptionGroup) as excinfo:
        print('\nException #1 in testExceptionOne before Calling...')
        fun()
        print('\nException #2 in testExceptionOne After Calling...')
        assert  excinfo.group_contains(RuntimeError)
        assert  excinfo.group_contains(TypeError)
        assert not excinfo.group_contains(SystemError)
        assert not excinfo.group_contains(SystemExit)
