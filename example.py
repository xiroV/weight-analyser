from wanalyser import WAnalyser

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

wanalyse = WAnalyser()
wanalyse.height = height
wanalyse.weight = weight
wanalyse.age = age
wanalyse.sex = sex


print('''
Your BMI is %d, which means that you are %s.\n
Your ideal weight is somewhere between %d and %d kg.
''' % (wanalyse.bmi(), wanalyse.bmi_category(), wanalyse.ideal_weight()[0], wanalyse.ideal_weight()[1]))

bmi_cat = wanalyse.bmi_category()
if bmi_cat != False:
    print('This means that you still need %s kg to reach normal weight.' % (wanalyse.weight_left()))

print('''
Your body fat estimate is %d kg.\n
This is approximately %d percent of your body weight which is %s.
''' % (wanalyse.body_fat()[1], wanalyse.body_fat()[0], wanalyse.body_fat()[2]))
