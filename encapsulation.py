
# This is working on encapsulation
class Protection:
    def __init__(self):
        # Setting a private variable
        self.__privateVar = 10
        # Setting a protected variable
        self._protectedVar = 13

    # setting teh modules to print them with formatting
    def getPrivate(self):
        print('Private: {}'.format(self.__privateVar))
    def getProtected(self):
        print('Protected: {}'.format(self._protectedVar))

if __name__ == "__main__":
    # Setting and printing the private variable
    pri = Protection()
    pri.getPrivate()

    # Setting and printing the protected variable
    pro = Protection()
    pro.getProtected()
    
