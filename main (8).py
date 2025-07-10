'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
import string

pass_len=8 
charvalues=string.ascii_letters+string.digits+string.punctuation

password=" "
for i in range (pass_len):
    password+=random.choice(charvalues)
    
    print("your random password is:",password)