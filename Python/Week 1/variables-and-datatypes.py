

print('Welcome to python');

# Data types in python include

# VARIABLES AND DATATYPES
name = 'alex' # string(str) data type
age = 100 # integer(int) data type
pi = 3.14 # Floating point(float) data type
isMale = True # Boolean(bool) data type
grades = {"Math": 40, "Physics": 60} # Dictionary(dict) data type
favMeals = ["Rice", "More Rice"] # Array(list) data type 
setType = {1,2,3,4}


# TYPE CONVERSION
isName = bool(name);
decimalAge = float(age);
integerPi = int(pi);

print(isName, decimalAge, integerPi);


# ACCEPTING USER INPUT
firstName = input('What is your first name? ')
userAge = input('What is your age? '); # we cannot use this age for arithmetic operations because by default the value of the input is a string, so we need to convert it to an int or a float before we use it.
# To do this, we could immediately wrap the input with the type we want to convert to, or we wrap the variable.

print(f"Hello {firstName}!");

# print(f"In 10 years, you will be {userAge + 10}") # let's see if implicit type coercion works here.

# Apparently, python doesn't do implicit type coercion, so this gives an error print(f"In 10 years, you will be {userAge + 10}"), because none of the values are converted to a matching type and we can't concatenate a string with an integer

print(f"In 10 years, you will be {int(userAge) + 10}")


# EXERCISE: Shopping Cart Program

item = input("What item are you selling? ");
price = float(input(f'Enter the price of 1 {item}: '));
quantity = int(input(f"How many {item}(s) are you selling? "));

sellingPrice = price * quantity

print(f"Selling {quantity} {item}(s), each for {price} will give you a total amount of {sellingPrice}")