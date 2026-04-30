def calculate_bmi(height, weight):

    print("Height = " , float(height))

    print("Weight = " , float(weight))
    
    bmi = weight/height * height
    print(f"BMI = {bmi:.3f}")
    if(bmi<18.5):
        print("You are underweight")
    elif(25.0>=bmi>=18.5):
        print("You have a normal BMI")
    elif(bmi>25):
        print("You are obese")

calculate_bmi(1.73,57)