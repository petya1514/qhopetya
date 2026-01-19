# Calculate BMI
name=input("What is your name?")
height=float(input("How tall are you (in meters)?\n"))
weight=float(input("How much do you weigh (in kilograms)?\n"))
age=input("How old are you (in years)?\n")
print()
bmi = weight / (height ** 2)
print(f"{name} and your BMI {bmi:.2f} and {age}")


