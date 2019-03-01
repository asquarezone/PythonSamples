# Largest prime factor
# https://projecteuler.net/problem=2
import datetime

def isPrime(number):
    isPrime = True
    print(f"checking whether factor {number} is prime or not")
    for index in range(2,number//2):
        if number%index == 0:
            isPrime = False
            return isPrime
    return isPrime

currentDT = datetime.datetime.now()
print (str(currentDT))
number = 600851475143
for index in range(number//2,2,-1):
    print(f"checking if {index} is factor of {number} or not")
    if number%index == 0:
        if isPrime(index):
            print(f"largest prime factor is {index}")
            break
print("finished execution")
currentDT = datetime.datetime.now()
print (str(currentDT))
