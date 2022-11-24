#using time and tqdm module to create result compiler symbol
from time import sleep
from tqdm import tqdm
import sys
# modules for colored title text
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint, colored 
from pyfiglet import figlet_format

cprint(figlet_format('SANITY', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Do you feel like doing things isn't fun anymore?\n(a) Not at all\n(b) Somewhat\n(c) Very much\n",
    "I have been feeling anxious of late\n(a) Not at all\n(b) Somewhat\n(c) Very much\n",
    "I often feel worried\n(a) Not at all\n(b) Somewhat\n(c) Very much\n",
    "I have a strong support system that helps me cope\n(a) Strongly disagree\n(b) Somewhat\n(c) Strongly agree\n",
    "I feel like a have a purpose in life\n(a) Strongly disagree\n(b) Somewhat\n(c) Strongly agree\n",
    "Feeling low, hopeless or depressed?\n(a) Not at all\n(b) Somewhat\n(c) Very much\n",
    "Are you having trouble managing your work, or getting along with others?\n(a) Not at all\n(b) Somewhat\n(c) Very much\n",
    "I still have a number of things to accomplish\n(a) Strongly disagree\n(b) Somewhat\n(c) Strongly agree\n",
    "I believe the things I do make a difference.\n(a) Strongly disagree\n(b) Somewhat\n(c) Strongly agree\n"


]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "c"),


]


def run_quiz(questions):
    
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            score_percent = score / len(questions) * 100
            # Compiler symbols
    for i in tqdm(range(3)):
        print("Compiling Results")
        sleep(1)
    print(f"Thank you for checking in! Your percentage wellbeing today is {score_percent}%")

def menu():
    entry_screen = input("Welcome to Sanity!\n Select [a] Get started! [b] About [c] Credits\n -> ").lower()
    return entry_screen

entry_screen = menu()

if entry_screen == "a":
    cprint('To get started\n You have a number of questionnaires and you can just answer by simply typing a, b or c...\n ', 'green', attrs=['bold'], file=sys.stderr)
    run_quiz(questions)
    menu()

if entry_screen == "b":
    cprint('Welcome to SANITY, your mental health checker...\n Sanity is a health terminal-app built with python that accept answers to questions as input and analysis the mental state of the user in seconds\n ', 'green', attrs=['bold'], file=sys.stderr)
    menu()
if entry_screen == "c":
    cprint('Credit Goes to Negpod7 May SE 2022:\n  Jeff Dauda\n Boris Nyilindek\n Elvis Kinyua\n Fese Mbile\n Diana Otieno\n Teny Gatluak, ', 'green', attrs=['bold'], file=sys.stderr)
    menu()


