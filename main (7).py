'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import random
 
target=random.randint(1,100)
while True:
    userchoice=input("Guess the target or quit:")
    if(userchoice=="quit"):
        break
    
    userchoice=int(userchoice)
    if(userchoice==target):
        print("success:correct guess!!")
        break
    elif(userchoice < target):
          print("your number was too small.take a bigger guess..")
        
    else:
        
        print("your number was too big.take a smaller guess..")
        
        print("___game over____")