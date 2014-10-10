from banalyser import BAnalyser

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

banalyse = BAnalyser()
banalyse.height = height
banalyse.weight = weight
banalyse.age = age
banalyse.sex = sex


print('''
Your BMI is %s, which means that you are %s.\n
Your ideal weight is somewhere between %s and %s kg.
''' % (str(banalyse.bmi()), str(banalyse.bmi_category()), str(banalyse.ideal_weight()[0]), str(banalyse.ideal_weight()[1])))

bmi_cat = banalyse.bmi_category()
if bmi_cat != False:
    print('This means that you still need %s kg to reach normal weight.' % (banalyse.weight_left()))

print('''
Your body fat estimate is %s kg.\n
This is approximately %s percent of your body weight which is %s.
''' % (str(banalyse.body_fat()[1]), str(banalyse.body_fat()[0]), banalyse.body_fat()[2]))
