class User:

    userList = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.isLoggedin = False

    def createUser(user_name, password):
        """
        docstring
        """
        newUser = User(user_name, password)
        return newUser

    def login(user_name, ):
        """
        docstring
        """
        if isLoggedIn == True:
            self.isLoggedIn = True
            print("Logged in Successfully")

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

        print("Welcome to password Locker.An application that will help you manage your passwords and even generate new passwords.")
        while True:
            print(
                "Use these short code to proceed:\n\n 1. cc-Create new Account\n 2. lg-Login\n 3. ex-exit")
            shortCode = input().lower()

            if shortCode == 'cc':
                print("New Account")
                print("*"*50)
                print("Username")
                user_name = input()
                print("Password")
                password = input()

                createUser = User.createUser(user_name, password)
                User.saveUser(createUser)
                print("\n")
                print(
                    f"Hi {user_name} Your Account has been created sucessfully")
                break

            elif shortCode == 'lg':
                print("*"*100)
                print("Enter your username and password")
                print("*"*100)

                print("Username")
                user_name = input()
                print("Password")
                password = input()

                for user in User.userList:
                    if user_name == user.user_name:
                        # User.login()
                        print("Break")
                break

            elif shortCode == 'ex':

                print("Bye. See you some other time.")
            
            else:
                print("Invalid shortcode\n")

        while True:
            print("What would like to do?\n\n Use these shortcodes to proceed\n 1. nc - Create new Credential \n 2. ds - Display existing Credential\n 3. fc - Find a credential \n 4. dc = Delete an existing Credential \n 5. ex - Exit Application")

            

            break
