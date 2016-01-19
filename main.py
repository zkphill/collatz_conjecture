'''
Created on Jan 18, 2016

@author: zkphi
'''

# collatz conjuecture calculator

# output file
fout = open("output.txt", "w")

# bounds for range of input numbers


# takes input and sends to odd or even function
def collatz_calculator(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1




# tests collatz calculator
def collatz_test(lower_bound, upper_bound):
    for num in range(lower_bound, upper_bound):
        fout.write(str(num) + " ")
        while num > 1:
            num = collatz_calculator(num)
            fout.write(str(num) + " ")
        fout.write("\n" + "\n")

lower_bound = input("enter the first number : ")
upper_bound = input("enter last number : ") + 1
  
collatz_test(lower_bound, upper_bound)
        
fout.close()