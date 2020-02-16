


# original meal price
meal_cost = float(input())
# tip percentage
tip_percent = int(input())
# tax percentage
tax_percent = int(input())
# Write your calculation code here
tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_cost = int(round(meal_cost + tax + tip))
# Print your result
print(str(total_cost))

