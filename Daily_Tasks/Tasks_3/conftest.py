def pytest_addoption(parser):
    parser.addoption("--test-one", action="store", default="default value", help="an optional argument for testing")
    
    parser.addoption("--dir", action="store", default="./", help="directory path to use for testing")

