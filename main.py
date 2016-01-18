'''
Created on Jan 18, 2016

@author: zkphi
'''

# collatz conjuecture calculator

# processes even numbers
def collatz_even(num):
    return num // 2

# processes odd numbers
def collatz_odd(num):
    return num * 3 + 1

# takes input and sends to odd or even function
def collatz_main(num):
    if num % 2 == 0:
        return collatz_even(num)
    else:
        return collatz_odd(num)

num = 33

print str(num)

# tests main function
while num > 1:
    num = collatz_main(num)
    print str(num) 