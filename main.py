'''
Created on Jan 18, 2016

@author: zkphi
'''

# collatz conjuecture calculator


fout = open("output.txt", "w")

# bounds for range of input numbers
lower_bound = 1
upper_bound = 101

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


# tests main function

def collatz_test(lower_bound, upper_bound):
    for num in range(lower_bound, upper_bound):
        fout.write(str(num) + " ")
        while num > 1:
            num = collatz_main(num)
            fout.write(str(num) + " ")
        fout.write("\n" + "\n")
    
collatz_test(lower_bound, upper_bound)
        
fout.close()