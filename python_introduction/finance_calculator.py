#!/usr/bin/python3

x = input("Enter your monthly income: ")
y = input("Enter your total monthly expenses: ")

monthly_saving = int(x) - int(y)

projected_saving = (monthly_saving * 12) + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are {monthly_saving}.")
print(f"Projected savings after one year, with interest, is: {int(projected_saving)}.")