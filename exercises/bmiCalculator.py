# Below 18.5	Underweight
# 18.5 - 24.9	Normal weight
# 25.0 - 29.9	Overweight
# 30.0 and above	Obesity

# meters= inches/39.37inches​

# BMI is calculated by dividing a person's weight in kilograms by the square of their height in meters (BMI = weight / height^2).

weight = int(input('What is your weight in kg: '))
height = int(input('What is your height in inches: '))

def bmi(a, b):
    heightInMeter = (height/39.37)**2
    totalBMI = weight/heightInMeter
    rounded = round(totalBMI, 2)
    
    if rounded <= 18.5:
        print(f'Your BMI is {str(rounded)}, and you are underweight!')
        print(f'Go hit your kitchen!')
    elif rounded <= 24.9:
        print(f'Your BMI is {str(rounded)}, and you are normal weight!')
    elif rounded <= 29.9:
        print(f'Your BMI is {str(rounded)}, and you are over weight!')
    else:
        print(f'Your BMI is {str(rounded)}, you are obese!')
        print('Hit your local gym')

bmi(weight, height)


