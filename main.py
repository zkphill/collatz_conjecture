'''
Created on Jan 18, 2016

@author: zkphi
'''

# collatz conjuecture calculator


# implements the collatz conjucture algorithm
def collatz_calculator(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1

# tests collatz calculator
# and counts the number of steps for all numbers
# in the input range
def collatz_test(lower_bound, upper_bound):
    num_steps = 0
    for num in range(lower_bound, upper_bound):
        
        while num > 1:
            num = collatz_calculator(num)    
            num_steps += 1
    return num_steps


lower_bound = input("enter the first number : ")
upper_bound = input("enter last number : ") + 1

num_steps = collatz_test(lower_bound, upper_bound)
average_num_steps = float(num_steps) / ((upper_bound - lower_bound))  

print "Number of steps: " + str(num_steps) + ", " \
        " Average number of steps: "+ str(average_num_steps)