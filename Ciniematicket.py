FULL_PRICE = 6.0
age = int(input("Enter your age: "))
if age < 16:
    ticket_price = FULL_PRICE / 2
elif age >= 60:
    ticket_price = FULL_PRICE / 3
else:
    ticket_price = FULL_PRICE
print(f"Your ticket costs £{ticket_price:}")