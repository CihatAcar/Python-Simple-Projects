"""
Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
numbers = [1,2,3,4,5,6,7,8,9]


def number_counter():
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Number of even number is %d and odd number is %d." %(odd, even))


number_counter()
