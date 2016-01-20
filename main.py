'''
Created on Jan 18, 2016

@author: zkphi
'''
import timeit

# collatz conjuecture calculator


# implements the collatz conjucture algorithm
def collatz_calculator(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1

# tests collatz calculator
def collatz_test(upper_bound, lower_bound):
    for num in range(lower_bound, upper_bound):
        while num > 1:
            num = collatz_calculator(num)    

lower_bound = input("enter the first number : ")
upper_bound = input("enter last number : ") + 1

print "start"

# calculates runtime  
t = timeit.Timer(lambda: collatz_test(upper_bound, lower_bound))

print t.timeit(number = 1)