# Name: Couassi Dzogbessi
# Date: 09/17/2026
# Course: COMP 163
# Project 1: Paycheck Calculator

# Put your name after "# Name:" above. The grader checks that it is filled in.

# Read four values from the user, in this order:
#   1. Employee name
name = input('Enter employee name: ')
#   2. Hours worked
hours = float(input('Enter hours worked: '))
#   3. Hourly rate
rate = float(('Enter hourly rate: '))
#   4. Tax rate, as a percent (for example, 10 means 10%)
tax_rate = float(input('Enter tax rate (Enter as a %): '))
#
# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
# Then calculate:
#   gross pay     = hours worked * hourly rate
gross_pay = hours * rate
#   tax withheld  = gross pay * (tax rate / 100)
tax_withheld = gross_pay * (tax_rate / 100)
#   net pay       = gross pay - tax withheld
net_pay = gross_pay - tax_withheld
#
# Then print the four required output lines.
print(f'Employee: {name}')
print(f'Gross pay: ${gross_pay:.2f}')
print(f'Tax withheld: ${tax_withheld:.2f}')
print(f'Net pay: ${net_pay:.2f}')
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
git add paycheck.py
git push 
