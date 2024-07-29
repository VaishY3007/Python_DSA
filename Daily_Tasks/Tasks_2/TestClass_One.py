class TestClassOne:
    myData = 0
    def testOne(self,setupTearDown):
        self.myData = 1
        print(f'\n in testOne() myData : {self.myData}')
        assert True
    def testTwo(self, setupTearDown):
            print(f'\n in testTwo() myData : {self.myData}')
            assert True