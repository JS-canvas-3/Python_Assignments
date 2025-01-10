weight = float(input("Enter your weight in (kg):"))
height = float(input("Enter your height in (m):"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 24.9:
    category = "normal"
elif 25 <= bmi <= 29.9:
    category = "overweight"
else:
    category = "obese"
print(f"Your BMI is: {bmi:}")
print(f"You are in the \"{category}\" range.")