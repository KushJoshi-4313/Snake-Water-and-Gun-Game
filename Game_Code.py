import random
from typing import SupportsComplex

def check(Computer,user):
   if (Computer == user):
    return 0

   if (Computer == 0 and user == 1):
     return -1

   if (Computer == 1 and user == 2):
     return -1

   if (Computer == 2 and user == 0):
     return -1

   return 1

 Computer = random.randint(0,2)
 user = int(input("0 for snake,1 for Water,2 for Gun :- "))

 score = check(Computer,user)
 print(Computer)
 if (score==0):
   print("No one wins")
 elif(score ==-1):
   print("Ypu loss")
 else:
   print("You win")
