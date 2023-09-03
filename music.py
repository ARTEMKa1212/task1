from math import *
print("type a number: ")
num1 = float(input())
print("Is this number in √")
answer = input()
if answer == "yes":
    num1 = sqrt(num1)
else:
    num1 = num1

print("type a number again: ")
num2 = float(input())
print("Is this number in √")
answer1 = input()
if answer1 == "yes":
    num2 = sqrt(num2)
else:
    num2 = num2
num1 = round(num1, 2)
num2 = round(num2, 3)
num_under_1 = 6.6324
num_under_2 = 0.46341

task = abs(num1 - num_under_1)
print(task)
task2 = abs(num2 - num_under_2)
print(task2)

task3 = abs(task / num_under_1)
print(task3)

task4 = abs(task2 / num_under_2)
print(task4)

if task3 > task4:
    print(" 19/44 is more precise")
else:
    print(" sqrt(44) is more precise")