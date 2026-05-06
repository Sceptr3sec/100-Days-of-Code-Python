weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal")
elif 25 <= bmi < 29.9:
    print("Overweight")