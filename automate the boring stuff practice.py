# - automate the boring stuff with python 

# CHAPTER 2 - flow control 
# figure 2-3
name = "Alice"

if name == "Alice":
    print("Hi Alice.")
else:
    print("Hello Stranger")
    
##--------------------------------
# figure 2-4
name = "Jordan"
age = 8

if name == "Alice":
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.")
    
##--------------------------------
# figure 2-5
name = "Kendrick"
age = 120

if name == "Alice": #false
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.") #false
elif age > 2000:
    print("Unlike you, Alice is not an undead, imortal vampire.") #false
elif age > 100:
    print("You are not Alice, grannie.") # executes here
    
##--------------------------------
# figure 2-6
name = "Kendrick"
age = 12000

if name == "Alice": #false
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.") #false
elif age > 100:
    print("You are not Alice, grannie.") # executes here because meets this condition first
elif age > 2000:
    print("Unlike you, Alice is not an undead, imortal vampire.")
    
##--------------------------------
# figure 2-7
name = "Kendrick"
age = 31

if name == "Alice": #false
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.") #false
else:
    print("You are neither Alice nor a little kid") # executes here
    
##--------------------------------

# figure 2-8

spam = 0

if spam < 5:
    print("Hello, World.") # executes once as its not a while loop
    spam = spam + 1
    
##--------------------------------
# figure 2-9

spam = 0
while spam < 5:
        print("Hello, World.") #prints 5 times when spam = 0-4
        spam = spam + 1 

##--------------------------------
# figure 2-10

name = " "

while name != "your name": 
    print("Please type your name.")
    name = input() #input name
else:
    print("Thank you!") # only executes if name = your name otherwise keeps asking you to type your name
    
##--------------------------------
# figure 2-11

while True:
    print("Please type your name")
    name = input()
    if name == 'your name': #condition required, otherwise
        break # break clause exits the loop and prints thank you!
print('thank you!')  

##--------------------------------
# figure 2-12

while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue # causes the programme to jump back to the start of the loop
    else: 
        print("Hello, Joe. What is the password? (It is a fish.)") # if name is Joe
        password = input()
        if password == "swordfish": # if not swordfish goes back to loop who are you
            break # only if swordfish breaks the loop and prints Access granted
print("Access granted.")

##--------------------------------
# figure 2-13

print("My name is")
for i in range (5): # starts the loop 0, 1, 2, 3, 4 (indexes)
    print("Jimmy Five Times (" + str(i)+ ")")

##--------------------------------
# figure 2-1

while True:
    print("is it raining?")
    is_raining = input()
    if is_raining == "no":
        break # exit loop go outside
    elif is_raining == "yes":
        print("do you have an umbrella?")
        have_umbrella = input()
        if have_umbrella == "yes":
            break # exit loop go outside
        else:
            while True: # create another loop because if its still raining you have to wait
                print("wait a while...")
                print("is it still raining?")
                still_raining = input()
                if still_raining == "yes":
                    continue # if still raining continue i.e. wait a whil..
                else:
                    break # exit loop go outside
print("go outside")

# -------------------------------

##--------------------------------
# random module generator
import random 

for i in range(5): # loop 5 times
    print(random.randint(1,10)) # prints random integers between 1-10 5 times

##--------------------------------
# Ending the programme early with the sys function

# can terminate/end programme before the last instruction using sys.exit() function

import sys 

while True:
    print("type exit to exit")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + ".")

##--------------------------------

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # correct guess

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

# ------------------------------------------------------------------
# rock, paper, scissors game:

import random, sys

# set up scoreboard
wins = 0
losses = 0
draws = 0

while True:
    print("%s Wins, %s losses, %s draws" %(wins, losses, draws))
    while True:
        print("Enter your move..(r)ock, (p)aper, (s)cissors or (q)uit")
        PlayerMove = input()
        if PlayerMove == 'r' or PlayerMove == 'p' or PlayerMove == 's':
            break 
        elif PlayerMove == 'q':
            sys.exit()
        
    # enter what player chooses
    print("type one of r, p, s, or q")
    if PlayerMove == "r":
        print("Rock verses..")
    elif PlayerMove == "p":
        print("Paper verses..")
    elif PlayerMove == "s":
        print("Scissors verses..")   
            
        #computer choice
    randomchoice = random.randint(1,3) # 3 choices
    if randomchoice == 1:
        computer = "r"
        print("ROCK")
    elif randomchoice == 2:
        computer = "p"
        print("PAPER")
    elif randomchoice == 3:
        computer = "s"
        print("SCISSORS")

        # update scores
    if PlayerMove == computer:
        print("Its a tie")
        draws = draws + 1
    elif PlayerMove == "r" and computer == "s":
        print("You win")
        wins = wins + 1
    elif PlayerMove == "r" and computer == "p":
        print("You lose")
        losses = losses + 1
    elif PlayerMove == "p" and computer == "r":
        print("You win")
        wins = wins + 1
    elif PlayerMove == "p" and computer == "s":
        print("You lose")
        losses = losses + 1
    elif PlayerMove == "s" and computer == "p":
        print("You win")
        wins = wins + 1
    elif PlayerMove == "s" and computer == "r":
        print("You lose")
        losses = losses + 1
            
#---------------
# q9 practice question flow control:
# is spam = 1 print Hello, if spam = 2 print howdy if anything else print greetings!

print("type a number") 
spam = int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    
#---------------
# q13 practice question flow control:
# write programme thats prints numbers 1 to 10 in for loop and do same in while loop

for numbers in range(1,11):
    print(numbers)
    
# using while loop
numbers = 0 # initialise counter
while numbers < 11:
        print(numbers)
        numbers = numbers + 1
        
#------------------------------------------------------------------------------------------      
# CHAPTER 3 FUNCTIONS

def hello():
    print("howdy!")
    print("howdy!!!")
    print("howdy!!!!")

hello()

#------------

def hello(name):
    print("Hello " + name)

hello("Jordan")

#------------ practice

def ShoppingList(items):
        print("I need to buy: " + items)

ShoppingList("bread, milk, spinach.")

#------------

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain' # return keyword specifies what return statement value should be
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
print(r)
fortune = getAnswer(r)
print(fortune)

#-----------------

def LeaguePosition(Answer): #define function with paramteter Answer
    if Answer == 1:
        return "1st"
    elif Answer == 2:
        return "2nd"
    elif Answer == 3:
        return "3rd"
i = random.randint(1,3) # random number generator stored in i
result = LeaguePosition(i) # call the function and pass in i as the arguement

#--------------

def RandomItem(Fruit): # defined out function RandomItem and apssed in parameter Fruit
    if Fruit == 1:
        return "Apple"
    elif Fruit == 2:
        return "Blueberrys"
    elif Fruit == 3:
        return "Cherrys"
    elif Fruit == 4:
        return "Bananas"
    else:
        return "Grapes"
    
i = random.randint(1,7) # random number generator stored in i
print(i)
choice = RandomItem(i) # call function and use i as the arguement
print(choice)

# -------------------------
# calling various functions -- 
# print a starts > print b starts > print c starts > print c returns >
# print b returns > print d starts > print d returns > print a returns 
# this is done in order of call

def a():
    print("a() starts")
    b()
    d()
    print("a() returns")
def b():
    print("b() starts")
    c()
    print("b() returns")
def c():
    print("c() starts")
    print("c() returns")
def d():
    print("d() starts")
    print("d() returns")

a()
    
# ----------------- LOCAL AND GLOBAL SCOPES 

# global variables can be accessed anywhere
# local variables cannot be accessed globally

x = 6 # this variable has no apparent function but its not a global variable it just so happens that it is commited to memory before and function is called
def example(): # define function
    z = 5 # create variable z and assign value to it
    print(z) # print the value of z

example() # call the function

# ------------------
x = 6
def example():
    print(x)
example() # we are able to access this x via this function

# ------------------
x = 6
def example():
    print(x)
    print(x + 5)
    x+=6 # this causes the error add 6 to this variable 
example() # but people naively think because we can accees the variable x we can modify it
# UnboundLocalError: local variable 'x' referenced before assignment
# because x is not a global variable

# ------------------
# over come this turn x into a global variable

x = 6
def example():
    global x
    print(x)
    x+=5
    print(x)

example()

# ------------------
# build in scope = all variables accesisble as soon as we start python interpretor
print("jordan")
False = False
def
import 
as 
elif 
try 
break 
lambda 
# etc..... you don;t need to import anything to use them you can use them anywhere

# ------------------ 
# Global scope = file wide, can be used within that file one 
# anything defined on the first indentation automatically becomes global variable

x = 1 # global variable x
def foo():
    y = 12 # has a local variable y
    print(f"foo sees x equal to {x}") # get access to global variable x
    print(f"foo sees y equal to {y}") # get access to local variable y as its called wihtin the local scope
foo()

# ------------------ 

x = 1 # global variable x
def foo():
    x = 11 # has local varibale x
    print(f"foo sees x equal to {x}")
foo()

# x prints out 11 not 1 for x because its searching for the variable x first in the local scope then works its way outwards if its not there

# ------------------ 

x = 1 # global variable x
def foo():
    x = 11 # has local varibale x
    print(f"foo sees x equal to {x}") # prints out 11 as its searching firs tin the local scope
foo()
print(f"global sees x equal to {x}") # prints out 1 as its calling in the global scope

# ------------------ 

x = 1 # global variable x
def foo():
    global x # now we are telling python when we are referencing anything in the local scope related to x we are refering to the global x 
    x = 11 # this tells python > change x in the global scope to = 11
    print(f"foo sees x equal to {x}") # prints out 11 as its searching firs tin the local scope
foo()
print(f"global sees x equal to {x}") # prints out 11 now as we have alterered x in the global scope wihtin the local scope be defining global x

# ------------------ 

x = 1 # global variable x
def foo():
    global x # now we are telling python when we are referencing anything in the local scope related to x we are refering to the global x 
    x = 11 # this tells python > change x in the global scope to = 11
    print(f"foo sees x equal to {x}") # prints out 11 as its searching firs tin the local scope
foo()
print(f"global sees x equal to {x}") # prints out 11 now as we have alterered x in the global scope wihtin the local scope be defining global x

# ------------------ 

x = 1 # global variable x

def foo():
    global x 
    y = 12
    x = 11 
    print(f"foo sees x equal to {x}")
    print(f"foo sees x equal to {y}")

# create another funciton named bar
def bar():
    print(f"bar sees x equal to {x}") # because we changed the value of x in the foo funciton this still prints out x = 11 in the bar function
    # this is beacuse the foo funciton was called 1st and changed the global variable x
foo() # call the functions
bar() 

print(f"global sees x equal to {x}")


# ------------------ 
# playing with different scopes

x = 1 # global variable x
def outer():
    x = 2 # local variable x
    def inner():
        x = 3 # local variable x
        print(f"inner sees x equal to {x}") # prints 3
        return 
    inner() # call inner 
    print(f"outer sees x equal to {x}") # prints 2
    return 
outer() # call outer
print(f"global sees x equal to {x}") # 1

# ------------------ 

x = 1 # global variable x
def outer():
    x = 2
    def inner():
        print(f"inner sees x equal to {x}") # x = 2 as although there is no x locally > 1 indent outwards there is x = 2
        return 
    inner() # call inner 
    print(f"outer sees x equal to {x}") # prints 2
    return 
outer() # call outer
print(f"global sees x equal to {x}") # 1

# ------------------ 

# where x is only in the global scope

x = 1 # global variable x
def outer():
    def inner():
        print(f"inner sees x equal to {x}") # x = 1
        return 
    inner() # call inner 
    print(f"outer sees x equal to {x}") # x = 1
    return 
outer() # call outer
print(f"global sees x equal to {x}") # 1

# ----------------------------------

x = 1 # x now becomes 3
def outer():
    x = 2 
    def inner():
        global x # assigns the x = 1 as x = 3 i.e. saying change the global variable to 3
        x = 3
        print(f"inner sees x equal to {x}") 
        return 
    inner() 
    print(f"outer sees x equal to {x}")
    return 
outer()
print(f"global sees x equal to {x}")

# ----------------------------------

x = 1 # remains unchanged
def outer():
    x = 2 # changes to x = 3
    def inner():
        nonlocal x # assigns the x = 2 as x = 3 using nonlocal condition
        x = 3
        print(f"inner sees x equal to {x}") 
        return 
    inner() 
    print(f"outer sees x equal to {x}")
    return 
outer()
print(f"global sees x equal to {x}")

# ----------------------------

# try and except - exception handling 

def function(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError: #built in function
        print("divide by error")

# calling in the function by passing in the arguement for the call
print(function(0)) # prints error here when called by passing in 0 as the arguement
print(function(2)) # allows the code to still be run for all other arguements
print(function(4))
print(function(6))

# ----------------------------------

# LISTS []
catNames = [] #start off with blank list that can store any number cats
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are:')
for name in catNames:
    print(name)

catNames
# ------------------------------------
# DICTIONARIES


