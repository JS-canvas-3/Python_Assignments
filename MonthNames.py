months = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

month_number = int(input("Enter the month: "))
if 1 <= month_number:
    if 1 <= month_number <= 12:
        print(f"Month {month_number} is {months[month_number - 1]}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
        