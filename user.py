class User:

    userList = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        isLoggedin = False

    def createUser(self):
        """
        docstring
        """
        newUser = User(user_name, password)
        return newUser

    def login(self):
        """
        docstring
        """
        if userName == self.user_name and password == self.password:
            isLoggedIn = True
        else:
            isLoggedIn = False    

    def saveUser(self):
        """
        docstring
        """
        User.userList.append(self)

    @classmethod
    def displayUser(cls):
        """
        docstring
        """
        return cls.userList

    def deleteUser(self):
        """
        docstring
        """
        User.userList.remove(self)


class Credentials:
    
    credentials = []

    def __init__(self,account,accountUsername,accountPassword):
        """
        docstring
        """
        self.account = account
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    def saveCredential(self):
        """
        docstring
        """
        Credentials.credentials.append(self)

    def searchCredential(parameter_list):
        """
        docstring
        """
        pass

    def displayCredential(parameter_list):
        """
        docstring
        """
        pass

    def credentialExist(parameter_list):
        """
        docstring
        """
        pass

    def loginWithCredential(parameter_list):
        """
        docstring
        """
        pass

    def passwordGenerate(parameter_list):
        """
        docstring
        """
        pass


    if __name__ == "__main__":
        pass