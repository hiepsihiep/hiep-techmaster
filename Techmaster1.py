# Bai 1
print("\nBai 1\n")

# Nhap score
Sco = float(input("Score: "))

# Logic
if Sco >= 90:
    print("Grade is A")
elif Sco >= 80:
    print("Grade is B")
elif Sco >= 70:
    print("Grade is C")
elif Sco >= 60:
    print("Grade is D")
else:
    print("Grade is F")

# Bai 2
print("\nBai 2\n")

# Nhap chieu cao, can nang
Cao = float(input("Height (inches): "))
Cao *= 0.0254
Nang = float(input("Weight (pounds): "))
Nang *= 0.45359237

# Tinh BMI
BMI = Nang / (Cao * Cao)
print(BMI)

# Logic
if BMI < 18.5:
    print("Underweight")
elif BMI < 25.0:
    print("Normal")
elif BMI < 30.0:
    print("Overweight")
else:
    print("Obese")
