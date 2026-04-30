def calculate_bmi(height, weight):

    print("Height = " , float(height))

    print("Weight = " , float(weight))
    
    bmi = weight/height * height
    print(f"BMI = {bmi:.3f}")

calculate_bmi(1.73,57)