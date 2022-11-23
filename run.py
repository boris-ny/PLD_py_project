from functions import main
from time import sleep
from tqdm import tqdm


# Compiler symbol
#
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
                  "a", [], ["north", "northern"]),
        Question("Question 2: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 3: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 4: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 5: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 6: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 7: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 8: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 9: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
        Question("Question 10: Do you feel like doing things isn’t fun anymore?",
                  "a", [], ["north", "northern"]),
]
for question in quizQuestions:
    print(f"{question.questionText}?")
    userInput = input()
            # store answers in var called count
    count = 0
            # if answer corresponds with required output, count increases by 2, otherwise it gets a decrease by 1
    if (userInput.lower() == question.answer.lower()):
        count += 1
    else:
      pass
        
    if (userInput.lower() == question.answer.lower()):
        count += 1
    elif (question.alternateAnswers != None and userInput.lower() in question.alternateAnswers):
        count += 1
    else:
        pass
percentage_score = (count/10)*100
for i in tqdm(range(1)):
  print("Compiling Rsults\n")
  sleep(0.5)

print(f"Based on the analysis, you are {percentage_score}% Okay today!")
