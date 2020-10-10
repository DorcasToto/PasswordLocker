class User:

    userList = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.isLoggedin = False

    def createUser(self):
        """
        docstring
        """
        newUser = User(user_name, password)
        return newUser

    def login(self, isLoggedIn):
        """
        docstring
        """
        if isLoggedIn == True:
            self.isLoggedIn = True

        else:
            print("Check your log in credentials")

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

    def __init__(self, accountName, accountUsername, accountPassword):
        """
        docstring
        """
        self.accountName = accountName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    def saveCredential(self):
        """
        docstring
        """
        Credentials.credentials.append(self)

    def searchCredential(self, accountName):
        """
        docstring
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return credential
            print("No such an account")

        else:
            print("No credentials saved")

    def displayCredential(self):
        """
        docstring
        """
        return Credentials.credentials

    def credentialExist(self, accountName):
        """
        docstring
        """

        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return True
            print("No such an account")

        else:
            print("No credentials saved")

    def deleteCredential(self):
        """
        docstring
        """
        Credentials.credentials.remove(self)

    def loginWithCredential(self):
        """
        docstring
        """

        # if isLoggedIn == True:
        #     self.isLoggedIn = True

        # else:
        #     print("Check your log in credentials")

    def passwordGenerate(self):
        """
        docstring
        """
        pass

    def copypassword(parameter_list):
        """
        docstring
        """
        pass

    if __name__ == "__main__":

        print("Welcome to password Locker.An application that will help you manage your passwords and even generate new passwords")
        while True:
            print("use these short code to proceed:\n cc:Create new Account\n lg:Login")
            shortCode = input().lower()

            if shortCode == 'cc':
