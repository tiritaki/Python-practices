import math
from random import randint
import time
# userAge = int(input ("Enter your age: "))
# userLimit = 16
# passCode = "Cohort11"

# if userAge>userLimit:
#    print (f"You met minimum age requirements")
#    userCode= input ("Enter passcode: ")
#    if passCode==userCode:
#       print (f"Your code {userCode} is valid. Access granted!")
#    print("Sorry your code is not valid")
    
# print("closing")

import random

"Player 1"
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Die 1: {die1}, Die 2: {die2}")

dice = die1 + die2  # value from both dice
if dice == 12:
    dice = 0  # re-assign the value of dice to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player1Score = dice
print(f"Player 1 Score : {player1Score}")

"Player 2"
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

print(f"Die 1: {die1}, Die 2: {die2}")

dice = die1 + die2  # value from both dice
if dice == 12:
    dice = 0  # re-assign the value of dice to 0
    print("Disqualified")
else:
    if die1 == die2:
        dice = dice * 2
player2Score = dice
print(f"Player 2 Score : {player2Score}")

# check/compare the values held in player1Score against player2Score
if player1Score > player2Score:
    print(f"Player 1 rolled {player1Score} and is the winner! ")
else:
    if player1Score < player2Score:
        print(f"Player 2 rolled {player2Score} and is the winner! ")
    else:
        print(f"Its a draw! | Player 1 rolled {player1Score} | Player 2 rolled {player2Score}")

# radius = float (input ("Enter radius "))
# area = round((math.pi * radius **2),2)

# print (f"Area is {area}")

# randNumbers = randint(1,100)
# print (f"the random namber is {randNumbers}")

# time.sleep(5)

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# x = int(input ("Enter your age: "))
# assert type(x) == int
# for i in range (1,6):
#     print (i)

# arr=[]
# i = 1
# while i:
#   arr.append(i)
#   if i == 3:
#     break
#   i += 1
# print(arr)

# n = randint(1,10) 
# n1 = int(input("guess a no between 1 to 100\n")) 
# attempts=1
# while n!=n1:
#     if n1>n:
#         print("Too high! ")
#     if n1<n:
#         print("Too low! ")
#     attempts=attempts+1
#     n1=int(input("Enter the number"))
# print (f"You got it!, you have tried {attempts} attemps")

# from random import randint
# randomlist = []
# for i in range(0,5):
#    n = randint(1,30)
#    randomlist.append(n)
# print(randomlist)

# for i in randomlist:
#     if i%2:
#         print(i, "this is an even number")
#     else:
#         print(i, "this is an odd number")

# def username():
#     last_name=input("Enter your last name ")
#     print (f"Your last name is {last_name}")
    
# username()

# def mult_num ():
#     num1=int(input("Pls enter num1"))
#     num2=int(input("Pls enter num2"))
#     return (print(f"The result of multiplication is {num1*num2}"))

# mult_num()

# def multiply (arg1,arg2):
#     return arg1 * arg2

# multiply (5,6)
# from random import sample
# def rnd():
#   res = sample(range(1, 10), 6)
#   for i in res:
#     if i==5:
#         print("One of the numbers = 5")
#     else: 
#         print ("Sorry numbers are not 5, try again")

# rnd()


# from random import randint
# def comparison():
#     rand_number= int(input("pls ener number between 1-10"))
#     if rand_number==randint(1,10):
#         print ("your numbers are equal")
#     else:
#         print("try again")

# comparison()

# from subroutine import rnd

# rnd()

# mystring = "My string has 1"
# x= mystring.isdigit()
# print(x)

# txt = "50800"

# x = txt.isdigit()

# print(x)

# fullName=input("pls enter name")
# listOfNames="Jill Oleh Jane Lucy"
# if fullName in listOfNames:
#     print (f" {fullName} in the string ")
# else:
#     print ( (f" {fullName} not in the string "))
            
# list1 = ["Oz", "Phil", "Seus", "Dre"]
# addDr = ["Dr. " + i for i in list1]
# print (addDr)

# number = int(input("Enter any number: "))
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")

#     print(number, "is not a prime number")
    
# list1 = [1,2,3]
# list2 = [2,3,4]
# list3 = [3,4,5]
# totalList = list1+list2+list3
# newlist =[]
# for i in totalList:
#     if totalList.count(i)>1 and i not in newlist:
#         newlist.append(i)
# print(sorted(newlist,reverse=True))

# print((list1+list2)[:5])
