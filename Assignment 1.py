
#1.Write Python code that prints your name, student number and email address.
print("John J. Olickal  ST00145785  johnjolickal@gmail.com")

#2.Write Python code that prints your name, student number and email address using escape sequences.
print("John J. Olickal\nST00145785\njohnjolickal@gmail.com")

#3.Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.
num1 = 14
num2 = 7
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")

#4. Write Python code that displays the numbers from 1 to 5 as steps.
print("1\n2\n3\n4\n5")

#5.Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen: An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".
print("\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\".")

#6.Practice and check the output print.
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#7.  Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
num = 23
textnum = "57"
decimal = 98.3
print(type(num))
print(type(textnum))
print(type(decimal))
sum_variables = num + int(textnum) + decimal
print("Sum:", sum_variables)
print("Type of sum:", type(sum_variables))

#8. calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour.
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"There are {total_minutes} minutes in a year, calculated as follows: {days_in_year} days * {hours_in_day} hours/day * {minutes_in_hour} minutes/hour.")

#9. Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting. An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming")

