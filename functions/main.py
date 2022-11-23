
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

    class Question:

        def __init__(self, questionText, answer, multipleChoiceOptions=None, alternateAnswers=None):
            self.questionText = questionText
            self.answer = answer
            self.multipleChoiceOptions = multipleChoiceOptions
            self.alternateAnswers = alternateAnswers

        def __repr__(self):
            return '{' + self.questionText + ', ' + self.answer + ', ' + str(self.multipleChoiceOptions) + ', ' + str(self.alternateAnswers) + '}'


    quizQuestions = [
            # ...
            Question("Question 1: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 2: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 3: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 4: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 5: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 6: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 7: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 8: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 9: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
            Question("Question 10: Do you feel like doing things isn’t fun anymore?",
                    "yes", [], ["north", "northern"]),
        ]
    for question in quizQuestions:
        print(f"{question.questionText}?")
        userInput = input()
                # store answers in var called count
        count = 0
                # if answer corresponds with required output, count increases by 2, otherwise it gets a decrease by 1
        if (userInput.lower() == question.answer.lower()):
                count += 2
        else:
                count -= 1
        if (userInput.lower() == question.answer.lower()):
            print("That is correct!")
        elif (question.alternateAnswers != None and userInput.lower() in question.alternateAnswers):
            print("That is correct!")
        else:
            print(f"Sorry, the correct answer is {question.answer}.")

    # if the requirements have been met, redirect to the menu options
    while True:
        print("| Type a, b, or c to select an option |\n")
        account_ans = input(
            "choose:  [a] - Sign Up     [b] - Login      [c] - Quit\n ->  ").lower()

        if account_ans == "a":
            register()
        if account_ans == "b":
            login()
        if account_ans == "c":
            break

        while login() == True:
            print("| Type a, b, or c to select an option |\n")
        account_ans = input(
            "choose:  [a] - Start     [b] - View Result      [c] - Quit\n ->  ").lower()

        if account_ans == "a":
            print("start")

        if account_ans == "b":
            print(count)
        if account_ans == "c":
            break
