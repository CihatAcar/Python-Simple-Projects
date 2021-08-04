"""
Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
number1 = 0
number2 = 1
nth = 0

while nth <= 56:
    print(number1) 0
    nth = number1 + number2
    number1 = number2
    number2 = nth
    nth += 1
