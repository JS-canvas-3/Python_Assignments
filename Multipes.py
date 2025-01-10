num = int(input("Enter a number: "))
limit = int(input("Enter the limit of Multiples:"))
print(f"Multiples of {num} up to {limit}:")
for i in range(1, limit + 1):
    multiple = num * i
    print(multiple)