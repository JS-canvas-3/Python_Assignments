# def calculate(a, b=10, c=None):
#     if c is None:
#         print(a + b)
#     else:
#         print(a * b * c)
#
#
# calculate(5)
# calculate(5, 3)
# calculate(5, 3, 2)





# def filter_strings(strings):
#     return [s for s in strings if len(s) >= 5]
#
# strings = ["apple", "cat", "banana", "dog", "grape"]
# print(filter_strings(strings))

# expression = "3 * 5 + 2"
# result = eval(expression)
# print(result)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers = list(filter(is_prime, numbers))
# print(prime_numbers)



def to_uppercase(strings):
    return list(map(str.upper, strings))

strings = ["apple", "banana", "cherry"]
print(to_uppercase(strings))


