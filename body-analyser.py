import math

weight = input('Your weight (in kg): ')
height = input('Your height (in cm): ')
age = input('Your age: ')
sex = input('Your sex (m/f): ')

if sex == 'm':
    sex = 1
elif sex == 'f':
    sex = 0
else:
    print('Invalid sex given')
    exit()

# Calculate basic stuff
age = int(age)
height = float(height) / 100
bmi = float(weight) / math.pow(float(height), 2)

lower_ideal_weight = math.pow(float(height), 2) * 18.5
upper_ideal_weight = math.pow(float(height), 2) * 25

body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * sex) - 5.4

# Determine body fat percentage category
if sex == 1:
    if body_fat > 24:
        body_fat_cat = 'above average'
    elif body_fat < 18:
        body_fat_cat = 'below average'
    else:
        body_fat_cat = 'average'
else:
    if body_fat > 31:
        body_fat_cat = 'above average'
    elif body_fat < 25:
        body_fat_cat = 'below_average'
    else:
        body_fat_cat = 'average'

if bmi < 18.5:
    weight_left = lower_ideal_weight - float(weight)
    bmi_status = 'gain '+str(round(weight_left,2))
elif bmi >= 25:
    weight_left = float(weight) - upper_ideal_weight
    bmi_status = 'lose '+str(round(weight_left,2))

# Determine BMI category
if bmi < 15:
    bmi_cat = 'very severely underweight'
elif bmi >= 15 and bmi < 16:
    bmi_cat = 'severely underweight'
elif bmi >= 16 and bmi < 18.5:
    bmi_cat = 'underweight'
elif bmi >= 18.5 and bmi < 25:
    bmi_cat = 'normal weight'
elif bmi >= 25 and bmi < 30:
    bmi_cat = 'overweight'
elif bmi >= 30 and bmi < 35:
    bmi_cat = 'Obese Class I (Moderately obese)'
elif bmi >= 35 and bmi < 40:
    bmi_cat = 'Obese Class II (Severely obese)'
else:
    bmi_cat = 'Obese Class III (Very severely obese)'

print('\nYour BMI is '+str(round(bmi,2))+', which means that you are '+bmi_cat+'.\n')
print('Your ideal weight is somewhere between '+str(round(lower_ideal_weight,2))+' and '+str(round(upper_ideal_weight,2))+'kg.\n')
if bmi_status:
    print('This means that you still need to '+bmi_status+'kg to reach normal weight.\n')
print('Your body fat percentage estimate is '+str(round(body_fat,2))+'% which is '+body_fat_cat+'.')