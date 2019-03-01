# Multiples of 3 and 5
# https://projecteuler.net/problem=1
maxNumber = 1000
sum = 0
for index in range(3,1000):
    if index%3 == 0 or index%5==0:
        sum = sum + index
#print(f"The sum of multiples of 3 or 5 below 1000 is {sum}")
print("The sum of multiples of 3 or 5 below 1000 is")
print(sum)