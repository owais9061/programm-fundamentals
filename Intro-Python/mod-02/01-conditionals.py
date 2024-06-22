# Write a program that checks if a number is positive, negative, or zero and prints an appropriate message.

# number = input("Enter a number: ")

# try:
#     num = float(number)
#     if num > 0:
#         print(f"The number {num} is positive.")
#     elif num < 0:
#         print(f"The number {num} is negative.")
#     else:
#         print("The number is zero.")
# except ValueError:
#     print(f"{number} is not a valid number.")



# Write a program that compares two numbers and prints the larger one. If the numbers are equal, print a message saying they are equal.
# num1=input("Input first number: ")
# num2=input("Input second number: ")
# if (num1>num2):
#     print(f"{num1} is greater than {num2}")
# elif (num1<num2):
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} and {num2} both are equal")


# Write a program that takes a student's score as input and prints their grade based on the following criteria:
    #  - A: 90-100
    #  - B: 80-89
    #  - C: 70-79
    #  - D: 60-69
    #  - F: Below 60

# student_score=input("Enter the marks of Student: ")
# stud_scr=float(student_score)

# if(stud_scr>=90 and stud_scr<=100):
#     print(f"Student on {stud_scr} marks, got A Grade.")
# elif(stud_scr>=80 and stud_scr<=90):
#     print(f"Student on {stud_scr} marks, got B Grade.")
# elif(stud_scr>=70 and stud_scr<=80):
#     print(f"Student on {stud_scr} marks, got C Grade.")
# elif(stud_scr>=60 and stud_scr<=70):
#     print(f"Student on {stud_scr} marks, got D Grade.")
# else:
#     print("Student FAILED")


# Write a program that checks if a given year is a leap year. A year is a leap year 
# - if it is divisible by 4 but not by 100, 
# - except if it is divisible by 400.

# input_year=input("Enter the year: ")
# inp_yr=int(input_year)
# if(inp_yr%4==0 and inp_yr%100!=0):
#     print("It's a Leap Year")
# elif(inp_yr%400==0):
#     print("It's a Leap Year")
# else:
#     print("Soryy it's not Leap Year.")

# Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# Write a program that checks the strength of a password. The password must be at least 8 characters long, contain both uppercase and lowercase characters, at least one digit, and one special character. Print messages indicating the criteria the password does not meet.

# Write a program that simulates a basic ATM. The user can check their balance, deposit money, and withdraw money. Ensure that the user cannot withdraw more than their balance and display appropriate messages for each operation.

# Write a program that displays a menu with options to add, subtract, multiply, or divide two numbers. The user can select an option and input the numbers. The program should perform the selected operation and display the result. Ensure that division by zero is handled gracefully.