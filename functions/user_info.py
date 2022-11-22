
usernames = []
passwords = []
names = []
class Runners():
    

    
    def register():
        names.append(input("Enter your first and last name: "))
        usernames.append(input("Enter your username: "))
        passwords.append(input("Enter your password: "))


    def login():
        username = input("Enter your username: ")
        password = input("Enter your Password: ")
        if username in usernames and password in passwords:
            print("welcome")
            


        else:
            print("User not found!")


    while True:
        print("| Type a, b, or c to select an option |")
        account_ans = input("choose:  [a] - Sign Up     [b] - Login      [c] - Quit\n ->  " ).lower()
        
        if account_ans == "a":
            register()
        if account_ans == "b":
            login()
        if account_ans == "c":
            break
