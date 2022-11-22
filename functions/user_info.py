
usernames = ['admin']
passwords = ['admin']
names = ['admin']
class Runners():
    

    
    def register():
        names.append(input("Enter your first and last name: "))
        reg_name = usernames.append(input("Enter your username: "))
        reg_pass = passwords.append(input("Enter your password: "))
        print("Proceed to login...\n")


    def login():
        username = input("Enter your username: ")
        password = input("Enter your Password: ")
        if username in usernames and password in passwords:
            print(f"welcome {username}")
            


        else:
            print("User not found!")


    while True:
        print("| Type a, b, or c to select an option |\n")
        account_ans = input("choose:  [a] - Sign Up     [b] - Login      [c] - Quit\n ->  " ).lower()
        
        if account_ans == "a":
            register()
        if account_ans == "b":
            login()
        if account_ans == "c":
            break
