
## Write a Python program to read a file and display its contents
# def read_file(filename):
#     try:
#         with open("C:\\Users\\sneha\\Desktop\\Sample1.txt", 'r') as file1:
#             contents = file1.read()
#             print(contents)
#     except FileNotFoundError:
#         print("The file does not exist.")
# print(read_file("C:\\Users\\sneha\\Desktop\\Sample1.txt"))


## Write a Python program to copy the contents of one file to another file
# def copy_file(source, destination):
#     try:
#         with open("C:\\Users\\sneha\\Desktop\\Sample2.txt", 'r') as src:
#             contents = src.read()
#         with open("C:\\Users\\sneha\\Desktop\\Sample1.txt", 'w') as dest:
#             dest.write(contents)
#         print("File copied successfully.")
#     except FileNotFoundError:
#         print("The source file does not exist.")
# print(copy_file("C:\\Users\\sneha\\Desktop\\Sample2.txt","C:\\Users\\sneha\\Desktop\\Sample1.txt"))


## Write a Python program to read the content of a file and count the total number of words in that file.
# def count_words_in_file(filename):
#     try:
#         with open("C:\\Users\\sneha\\Desktop\\Sample2.txt", 'r') as file:
#             contents = file.read()
#             word_count = len(contents.split())
#             print(f"Total number of words: {word_count}")
#     except FileNotFoundError:
#         print("The file does not exist.")
# print(count_words_in_file("C:\\Users\\sneha\\Desktop\\Sample2.txt"))



## Write a Python program that prompts the user to input a string and converts it to an integer.
# def string_to_integer():
#     try:
#         user_input = input("Enter a string to convert to an integer: ")
#         converted_int = int(user_input)
#         print(f"Converted integer: {converted_int}")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer string.")
#
# print(string_to_integer())


## Write a Python program that prompts the user to input a list of integers
# and raises an exception if any of the integers in the list are negative.
# def validate_positive_integers():
#     try:
#         user_input = input("Enter a list of integers separated by spaces: ")
#         numbers = list(map(int, user_input.split()))
#         for number in numbers:
#             if number < 0:
#                 raise ValueError("Negative numbers are not allowed.")
#         print("All numbers are positive.")
#     except ValueError as e:
#         print(e)
#
# print(validate_positive_integers())





## Write a Python program that prompts the user to input a list of integers and computes the average.
# def compute_average():
#     try:
#         user_input = input("Enter a list of integers separated by spaces: ")
#         numbers = list(map(int, user_input.split()))
#         average = sum(numbers) / len(numbers)
#         print(f"Average: {average}")
#     except ValueError:
#         print("Invalid input. Please enter only integers.")
#     except ZeroDivisionError:
#         print("Cannot compute average for an empty list.")
#     finally:
#         print("Program has finished running.")
#
# print(compute_average())


## Write a Python program that prompts the user to input a filename and writes a string to that file.
# def write_to_file():
#     try:
#         filename = input("Enter the filename to write to: ")
#         content = input("Enter the content to write to the file: ")
#         with open(filename, 'w') as file:
#             file.write(content)
#         print("File written successfully. Welcome!")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# print (write_to_file())

