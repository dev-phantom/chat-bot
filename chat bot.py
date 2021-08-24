import random
print("hi am phantom")
greeting = ["hello","hi","good morning", "good afternoon","good evening", "welcome"]
leaving =["good bye", "sweet dreams", "bye!"]
question1 =["what's your name?","who owns you?", "who created you?", "how are you?", "how are you doing?","what's up?","hello","i have a question"]
answers =["am phantom your personal chat bot", "it's Favour he's a very great guy", "am fine","hi there","please go ahead"]
greetings=random.choice(greeting)
leave = random.choice(leaving)
name = input(str("what's your name please? "))
print(str(greetings)+" "+ name + " its nice meeting you")
def ask():
    question_1 = input(str("how may i help you? " + " " + name + " "))
    if (question_1 == question1[0]) :
        print(answers[0])
    elif question_1 == question1[1] or (question_1 == question1[2]):
        print(answers[1])
    elif (question_1 == question1[3]) or (question_1 == question1[4]) or (question_1 == question1[5]):
        print(answers[2])
    elif (question_1 == question1[6]):
        print(answers[3])
    elif(question_1 == question1[7]):
        print(answers[5])
    elif question_1 == "help":
        a = open("help.txt", "r")
        b = a.read()
        print(b)
    else:
        print("opps i didn't catch that try again or read our help doc")
ask()
def question():
    question_2 = input(str("would that be all for now? "))
    for x in range(10):
        if question_2 == "yes":
            print(name + " " + "thanks for veiwing me")
            print(leave)
            break
        elif question_2 == "no":
            return ask()
        else:
            return question()
question()