# Name: Ariana Fafach
# Date: 2/4/2026
# Title: Program #5: Hot Dog



# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

# Get input from user
type = input("Do you want a Hot dog or a Chili dog? Enter H for Hot dog and C for Chili dog: ")
onions = input("Do you want grilled onions? enter Y for yes and N for no: ")
cheese = input("Do you want cheese? enter Y for yes and N for no: ")
peppers = input("Do you want peppers? enter Y for yes and N for no: ")

# Calculate cost of dog
if type == 'H':
    cost_dog = 3.50
elif type == 'C':
    cost_dog = 4.50

# find cost of toppings
if onions == 'Y':
    cost_onions = 1.00
elif onions == 'N':
    cost_onions = 0

if cheese == 'Y':
    cost_cheese = 0.50
elif cheese == 'N':
    cost_cheese = 0

if peppers == 'Y':
    cost_peppers = 0.75
elif peppers == 'N':
    cost_peppers = 0

# Calculate total cost before tax
cost_before_tax = cost_dog + cost_onions + cost_cheese + cost_peppers
# Calculate tax
tax = (cost_before_tax) * 0.07
# Calculate total cost
total_cost = (cost_before_tax) + (cost_before_tax) * 0.07


# Display costs
print(f"Your cost before tax is ${cost_before_tax:.2f}")
print(f"Your tax is ${tax:.2f}")
print(f"Your total cost is ${total_cost:.2f}")
