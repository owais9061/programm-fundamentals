# THIS PYTHON file has all the code given to me by the professor.
# Some of this code is very basic and it's better to have a what you've learnt.

#1
#Here are my print statements that print 1 - 3
print("one")
print("two")
print("three")


#Here's a single line comment

"""Here's a
multi-line comment
on multiple lines"""



#2
"""This code will:
Prompt for your name
Set the 'name' variable
Print a message"""
name = input("What is your name?") #gets the user's name
print("Hello " + name) #prints a message with the user's name


#3
fav_movie = input("What is your favorite movie?")
fav_singer = input("Who is your favorite singer?")

favs = "Your favorite movie is {} and your favorite singer is {}".format(fav_movie, fav_singer)
print(favs)
# or
print(f"Your favourite movie is {fav_movie} & you're favourite singer is {fav_singer}.")


#4
fav_movie = "Jutt and Juliet 3"
fav_singer = "DIljit Dosanjh"

favs = "Your favorite movie is " + fav_movie + " and your favorite singer is " + fav_singer
print(favs)



#5
#define and set variables from user input (casted to a float)
bill = float(input("How much is the meal?"))
tax = float(input("What is the sales tax (percentage)?"))
tip = float(input("How much of a tip (percentage)?"))

#calculate and add tax
tax_amount = (bill * tax) / 100 #calculate the tax
total = bill + tax_amount #add tax amount to final bill

#calculate and add tip
tip_amount = (total * tip) / 100 #calculate the tip
total = total + tip_amount #add tip amount to final bill

#round the total to 2 decimal places
total = round(total, 2) #round the total amount

#print the final amount
print("The total bill is $", total, sep = '')

