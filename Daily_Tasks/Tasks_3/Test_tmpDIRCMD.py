import os
import pytest
from FileDir_Ops import createFile, createDir

# def pytest_addoption(parser):
#     parser.addoption("--dir", action="store", default="./", help="directory path to use for testing")

@pytest.fixture
def tmpDir(request):
    return request.config.getoption("--dir")

def testCreateDirectory(tmpDir):
    dirPath = os.path.join(tmpDir, 'MyDirNew1')
    assert not os.path.exists(dirPath)
    createDir(dirPath)
    assert os.path.exists(dirPath) and os.path.isdir(dirPath)

def testCreateFile(tmpDir):
    dirPath = os.path.join(tmpDir, 'MyDirNew1')
    createDir(dirPath)
    filePath = os.path.join(dirPath, 'aan.txt')
    assert not os.path.exists(filePath)
    createFile(filePath)
    assert os.path.exists(filePath) and os.path.isfile(filePath)

def myNameOne():
    assert True

def myNameTow():
    assert True
