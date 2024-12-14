#10.  Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($) An example runs of the program: Please enter amount in pounds: XXX £ XXX are $ XXX.
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * 1.27
print(f" {pounds} are $ {dollars:.2f}")