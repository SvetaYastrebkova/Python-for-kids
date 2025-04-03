# input mass
try:
    mass_kg = int(input("Введите вес в кг: "))
except ValueError:
    print("Ошибка: Введите вес в кг.")
    exit()

# input height
try:
    height_sm = int(input("Введите рост сантиметрах: "))
except ValueError:
    print("Ошибка: Введите рост сантиметрах.")
    exit()

# Convert height to meters

height_m = height_sm / 100

# calc BMI

bmi = mass_kg / ( height_m * height_m )

# Determine BMI category
if bmi < 16.0:
    category = "Underweight (Severe thinness)"
elif 16.0 <= bmi < 16.9:
    category = "Underweight (Moderate thinness)"
elif 17.0 <= bmi < 18.4:
    category = "Underweight (Mild thinness)"
elif 18.5 <= bmi < 24.9:
    category = "Normal range"
elif 25.0 <= bmi < 29.9:
    category = "Overweight (Pre-obese)"
elif 30.0 <= bmi < 34.9:
    category = "Obese (Class I)"
elif 35.0 <= bmi < 39.9:
    category = "Obese (Class II)"
else:
    category = "Obese (Class III)"

# output

print(f"Ваш индекс BMI: {bmi:.2f}")
print(f"Категория: {category}")
