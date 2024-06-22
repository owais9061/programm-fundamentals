# Write a program that prints numbers from 1 to 10 using a for loop.
for num in range(1,11):
    print(num)

# Write a program that calculates the sum of numbers from 1 to 100 using a while loop.
num = 1
sum = 0

while num <= 100:
    sum += num
    num += 1
print(f"The sum of numbers from 1 to 100 is: {sum}")


# Write a program that calculates the factorial of a given number using a for loop.
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")


# Write a program that counts the number of vowels in a given string using a while loop.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
index = 0
while index < len(string):
    if string[index] in vowels:
        count += 1
    index += 1
print(f"Number of vowels in the string: {count}")


# Write a program that prints the first 20 numbers in the Fibonacci sequence using a for loop.
a, b = 0, 1
print(a)

for _ in range(19):
    print(b)
    a, b = b, a + b

# Write a program that prints all prime numbers between 1 and 100 using a while loop.
number = 1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while number <= 100:
    if is_prime(number):
        print(number)
    number += 1



# Write a program that prints the following pattern using nested for loops:
    #  ```
    #  *
    #  **
    #  ***
    #  ****
    #  *****

# Number of rows in the pattern
num_rows = 5

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        print("*", end="")
    print()


# Write a program that multiplies two 3x3 matrices using nested for loops and prints the result.

# First matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Second matrix
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Result matrix
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Multiply matrices
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print result matrix
print("Result of matrix multiplication:")
for row in result:
    print(row)
