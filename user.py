class User:

    userList = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.isLoggedin = False

    def createUser(user_name, password):
        """
        method to create new user
        """
        newUser = User(user_name, password)
        return newUser

    def login(user_name, ):
        """
        method that allows a user to log in after providing credentials
        """
        if isLoggedIn == True:
            self.isLoggedIn = True
            print("Logged in Successfully")

        else:
            print("Check your log in credentials")

    def saveUser(self):
        """
        method that adds user to the list
        """
        User.userList.append(self)

    @classmethod
    def displayUser(cls):
        """
        method that displays saved users
        """
        return cls.userList

    def deleteUser(self):
        """
        method that delete a selected user
        """
        User.userList.remove(self)


if __name__ == "__main__":
    pass


class Credentials:

    credentials = []

    def __init__(self, accountName, accountUsername, accountPassword):
        """
        crede
        """
        self.accountName = accountName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    def saveCredential(self):
        """
        method that adds credentials to the list
        """
        Credentials.credentials.append(self)

    @classmethod
    def createCredential(self, accountName, accountUsername, accountPassword):
        """
        method that creates a new credential
        """
        newCredential = Credentials(
            accountName, accountUsername, accountPassword)
        return newCredential

    def searchCredential(accountName):
        """
        method that searches a new credential and returns the credential
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.accountName == accountName:
                    return credential
            print("No such an account")

        else:
            print("No credentials saved")

    def displayCredential():
        """
        methods to display all saved credentials
        """
        return Credentials.credentials

    def credentialExist(accountName):
        """
        method that checks if a credentials exists
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
        method that deletes a credential
        """
        Credentials.credentials.remove(self)

        """
        docstring
        """

        # if isLoggedIn == True:
        #     self.isLoggedIn = True

        # else:
        #     print("Check your log in credentials")

    def passwordGenerate(self):
        """
        method that generate a random password
        """
        pass

    def copypassword(parameter_list):
        """
        method that allows copying of password to keyboard
        """
        pass


if __name__ == "__main__":
    # a = Credentials.createCredential("","","")
    # print(str(a))

    print("Welcome to password Locker.An application that will help you manage your passwords and even generate new passwords.")
    while True:
        print(
            "Use these short code to proceed:\n\n 1. cc-Create new Account\n 2. lg-Login\n 3. ex-Exit")
        shortCode = input().lower()

        if shortCode == 'cc':
            print("New Account")
            print("*"*50)
            print("Username")
            user_name = input()

            while True:
                print(
                    "1. op - You want to type your own password?\n 2. sg - System generated passwords")
                passwordOption = input()

                if passwordOption == 'op':
                    print("Your Password")
                    password = input()
                    break
                elif passwordOption == 'sg':
                    Credentials.passwordGenerate()
                    break

                else:
                    print("PasswordOption Invalid")

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
            break

        else:
            print("Invalid shortcode\n")

    while True:
        print("What would like to do?\n\n Use these shortcodes to proceed\n 1. nc - Create new Credential \n 2. ds - Display existing Credential\n 3. sc - Find a credential \n 4. dc -  Delete an existing Credential \n 5. ex - Exit Application")

        shortCode = input().lower()

        if shortCode == 'nc':
            print("New Credential Account")
            print("*"*100)
            print("\n")

            print("Account Name e.g Facebook")
            AccountName = input()

            print("Account's UserName")
            accountUserName = input()

            while True:
                print(
                    "1. op - You want to type your own password?\n 2. sg - System generated passwords")

                PasswordOption = input().lower()

                if PasswordOption == 'op':
                    print("Account's Password :")
                    accountPassword = input()
                    break
                elif PasswordOption == 'sg':
                    Credentials.passwordGenerate()
                    break

                else:
                    print("Password Invalid")

            newC = Credentials.createCredential(
                AccountName, accountUserName, accountPassword)
            Credentials.saveCredential(newC)
            print("\n")
            print("Your Account's Credentials has been saved!")
            print("\n")

            # newC = Credentials(
            #     accountName, accountUserName, accountPassword)
            # newC.saveCredential()

        elif shortCode == 'ds':
            if Credentials.displayCredential():
                print("List of your credentials include:\n")
                for credential in Credentials.credentials:
                    accountName = credential.accountName
                    accountuser = credential.accountUsername
                    accountpass = credential.accountPassword
                    print(
                        f"Account Name : {accountName}\n Account Username : {accountuser}\n Account Password: {accountpass}\n")

            else:
                print("You do not have saved credentials at the moment ")

        elif shortCode == 'sc':
            print("Account name: ")
            AccountName = input()
            if Credentials.credentialExist(AccountName):
                searchAccount = Credentials.searchCredential(AccountName)
                print(
                    f"Account name: {searchAccount.accountName}\n Account's Username: {searchAccount.accountUsername}\n Account's Password : {searchAccount.accountPassword}")

            else:
                print("No such an account name!")

        elif shortCode == 'dc':
            print("Account name you would like to delete?")
            AccountName = input()
            if Credentials.credentialExist(AccountName):
                Credentials.deleteCredential(AccountName)
                print("Account Successfully deleted")

            else:
                print("No Account such an account name")

        elif shortCode == 'ex':
            print("Bye see you")

            break

        else:
            print("invalid short code")
