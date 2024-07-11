import math
import random
lower = int(input("enter the value of lower bound : "))
upper = int(input("enter the value of upper bound : "))
x = random.randint(lower,upper)
total_chances = math.ceil(math.log(upper - lower + 1 , 2 ))
print("you only have ", total_chances ,"to guess the number \n ")
count = 0
flag = False
while count<total_chances:
    count += 1
    guess=int(input("write your guesss :  "))
    if guess==x:
        print("congrats you did it in ", count , "try")
        flag = True
        break
    elif x > guess:
        print("oops number is to low ! ")
    elif x < guess:
        print("oops number is to high ! ")

if not flag:
    print(f"\n the number is {x} ")
    print("\t better luck next time ")          

