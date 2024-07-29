'''
Intro to nesting of functions
'''

def outerFun():
    print("Entering outer function")
    def innerFun():
        print("Entering inner function")
    innerFun() #Calling the Inner function
    print("Exiting from Outer function")
    
outerFun() #Calling the Outer function