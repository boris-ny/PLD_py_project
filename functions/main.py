
usernames = ['admin']
passwords = ['admin']
names = ['admin']
 


class Runners():
    # The runners class controls user funcs and is called outside by run.py
    # function to handle login

    def register():
        names.append(input("Enter your first and last name: "))
        reg_name = usernames.append(input("Enter your username: "))
        reg_pass = passwords.append(input("Enter your password: "))
        print("Proceed to login...\n")

    # function to handle signup
    def login():
        username = input("Enter your username: ")
        password = input("Enter your Password: ")
        # search list for user and passwords that match
        if username in usernames and password in passwords:
            print(f"welcome {username}")

        else:
            print("User not found!")

    def menu():
        pass   
