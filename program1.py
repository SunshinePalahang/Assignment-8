import random

def lottery():
#ask 3 numbers
    userNums = []
    for i in range(3):
        numbers = int(input("Pick a number from 0 to 9: "))
#no repetition and only from 0 to 9
        while (numbers in userNums or numbers<0 or numbers>9):
            print("Invalid. Pick again.")
            numbers = int(input("Pick a number from 0 to 9: "))
        userNums.append(numbers)    
lottery()