# Write a program that checks if a number is positive, negative, or zero and prints an appropriate message.

# number = input("Enter a number: ")

try:
    num = float(number)
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print(f"{number} is not a valid number.")



# Write a program that compares two numbers and prints the larger one. If the numbers are equal, print a message saying they are equal.
num1=input("Input first number: ")
num2=input("Input second number: ")
if (num1>num2):
    print(f"{num1} is greater than {num2}")
elif (num1<num2):
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} both are equal")


# Write a program that takes a student's score as input and prints their grade based on the following criteria:
    #  - A: 90-100
    #  - B: 80-89
    #  - C: 70-79
    #  - D: 60-69
    #  - F: Below 60

student_score=input("Enter the marks of Student: ")
stud_scr=float(student_score)

if(stud_scr>=90 and stud_scr<=100):
    print(f"Student on {stud_scr} marks, got A Grade.")
elif(stud_scr>=80 and stud_scr<=90):
    print(f"Student on {stud_scr} marks, got B Grade.")
elif(stud_scr>=70 and stud_scr<=80):
    print(f"Student on {stud_scr} marks, got C Grade.")
elif(stud_scr>=60 and stud_scr<=70):
    print(f"Student on {stud_scr} marks, got D Grade.")
else:
    print("Student FAILED")


# Write a program that checks if a given year is a leap year. A year is a leap year 
# - if it is divisible by 4 but not by 100, 
# - except if it is divisible by 400.

input_year=input("Enter the year: ")
inp_yr=int(input_year)
if(inp_yr%4==0 and inp_yr%100!=0):
    print("It's a Leap Year")
elif(inp_yr%400==0):
    print("It's a Leap Year")
else:
    print("Soryy it's not Leap Year.")


# Write a program that prints numbers from 1 to 100. 
# - For multiples of 3, print "Fizz" instead of the number, 
# - and for multiples of 5, print "Buzz". 
# - For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# Iterate over numbers from 1 to 100

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Write a program that checks the strength of a password. The password must be at least 8 characters long, contain both uppercase and lowercase characters, at least one digit, and one special character. Print messages indicating the criteria the password does not meet.
import string

# Function to check if a password meets the strength criteria
def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password should be at least 8 characters long."
    
    # Check for uppercase, lowercase, digit, and special character
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not has_upper:
        return "Password should contain at least one uppercase letter."
    if not has_lower:
        return "Password should contain at least one lowercase letter."
    if not has_digit:
        return "Password should contain at least one digit."
    if not has_special:
        return "Password should contain at least one special character."

    # If all criteria are met
    return "Password is strong."

# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)


# Write a program that simulates a basic ATM. 
# The user can check their balance, deposit money, and withdraw money. 
# Ensure that the user cannot withdraw more than their balance 
# and display appropriate messages for each operation.
print("WELCOME TO GUJJAR'S BANK")
print("=========================")
print("Select your desired action: \n 1- Check Balance \n 2- Deposit Money \n 3- Withdraw Money")
choose = input()
choice = int(choose)

# Balance
balance_opt = 233200
deposit_opt = 0
withdraw_opt = 0

if choice == 1:
    print("USER ACCOUNT BALANCE CHECK")
    print(f"Your current balance is {balance_opt}")
elif choice == 2:
    print("USER DEPOSIT ACCOUNT SECTION")
    print(f"Current Balance is {balance_opt}")
    depos_opt = input("How much do you want to deposit? ")
    deposit_opt = int(depos_opt)
    balance_opt += deposit_opt
    print(f"CONGRATULATIONS!! \n Your new account balance after deposit of {deposit_opt} is: {balance_opt}")
elif choice == 3:
    print("USER WITHDRAW SECTION")
    print(f"Current Balance is {balance_opt}")
    withd_opt = input("How much do you want to Withdraw? ")
    withdraw_opt = int(withd_opt)
    if withdraw_opt > balance_opt:
        print("SORRY!! \n Your Account does not have sufficient funds.")
    elif withdraw_opt == balance_opt:
        balance_opt -= withdraw_opt
        print("Your Balance will be 0 after this transaction. Transaction not possible.")
    else:
        balance_opt -= withdraw_opt
        print(f"CONGRATULATIONS!! You've withdrawn {withdraw_opt} amount and your new balance is {balance_opt}.")
else:
    print("PLEASE SELECT THE VALID OPTION !!")