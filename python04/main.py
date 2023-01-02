'''
Asking several questions and then creating a story 
with the user input. 
'''


name = input("What is your name? ")
action = input("What do you do for fun? ")
state = input("Where is the state you reside in? ")
age = input("How old are you? ")
sublingNum = input("How many sublings do you have? ")

print("Hello, my name is","\033[33m",name,"\033[0m",". ")
print("On my free time I like","\033[33m",action,"\033[0m", ". ")
print("I am",age, " and I have ","\033[33m",sublingNum,"\033[0m"," siblings.")
print("I currently live in the great state of","\033[33m",state,"\033[0m",".")
