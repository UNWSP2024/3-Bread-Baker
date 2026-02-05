# Name: Ariana Fafach
# Date: 2/3/2026
# Title: Program #3: Shipping Charges


# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	                            Price Per Pound
# 2 pounds or less   	                    $1.50
# Over 2 pounds but not more than 6 pounds  $3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	                        $4.75
# Write a program which calculates the shipping charge and displays the total.


# Get the number of packages from the user:
number = int(input("Enter the number of packages you have: "))

# For loop to get the weight of each of the packages from the user:
total_cost = 0
for i in range (1,number + 1):
    package_weight = float(input(f"Enter the weight in pounds of package number {i}: "))
    # if else statments to determine cost of current package.
    if package_weight <= 2:
        cost = package_weight * 1.5
    elif package_weight > 2 and package_weight <= 6:
        cost = package_weight*3
    elif package_weight > 6 and package_weight <= 10:
        cost = package_weight*4
    elif package_weight > 10:
        cost = package_weight*4.75
# Add the cost of current package to total_cost in order to get the total cost of all packages.
    total_cost += cost
# Print the result.
print(f"It will cost a total of ${total_cost:,.2f} to send your packages.")
