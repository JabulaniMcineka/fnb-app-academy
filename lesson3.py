# Adding two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")



print(sum(int(num1) + int(num2)))  # Output: 23 (addition of integers) type casting


#Core data types in python
# strings, integers, floats, booleans, lists, tuples, sets, dictionaries

# Type Casting
# converting one data type to another


#Mathematical operators
# +, -, *, /, %, **

# Calculating the tip

bill = float(input("Enter the bill amount: R"))
tip = 0.15 * bill  # 15% tip
val_tip = bill * tip
total_cost = bill + val_tip

print(f"Here is the tip amount: R{val_tip}")
print(f"Here is the total cost: R{round(total_cost, 2)} rounded to 2 decimal places ")