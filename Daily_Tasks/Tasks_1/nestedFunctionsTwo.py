'''
Intro to nesting of functions
'''

def outerFun():
    print("Entering outer function")
    def innerFun():
        print("Entering inner function")
    print("Exiting from Outer function")
    
    return innerFun()
res = outerFun()
res()
    
outerFun() #Calling the Outer function