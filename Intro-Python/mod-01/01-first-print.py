print("Owais Gujjar " ',' "is a Programmer")

#  Below are some the coding exercise I've done. Questions are genrated by GPT, but th logic and the solution is self written.

#  Write a Python script to print "Hello, World!" to the console.
print("Hello, World!")

#  Create a variable with your name and print "Hello, [Your Name]!".
name = "Owais"
print(f"Hello, {name}!")


#  Write a Python script to print the following information in a formatted way:
# Name: Owais
# Age: 20
# Country: Pakistan
name = "Owais"
age = 20
country = "Pakistan"
# print("Hey, I'm " , name , " I'm " , age , "yrs old, currently living in " , country);
print(f"Hey everyone, I'm {name}. I'm {age}yrs old & I'm currently living in {country}")

#  Create a list of your three favorite fruits and print each fruit on a new line.
fruits = ['Apple','Mango','Pineapple']
for fruit in fruits:
   print(fruit)


#  Create a script that asks the user for their name and age, and then prints a message saying, "Hello, [Name]! You are [Age] years old."
name1=input("Enter your Name Buddy: ")
age1=input("Enter your Age: ")
print(f"Hey, I guess your name is {name1} & your age might be {age1}")


#  Write a Python script to print a multiplication table from 1 to 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ");
    print();