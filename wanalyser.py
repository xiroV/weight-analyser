import math

class WAnalyser:
	def __init__(self):
		weight = 0
		height = 0
		age = 0
		sex = 0 # values: 0 = female, 1 = male
	
	# returns bmi of person	
	def bmi(self):
		return round(float(self.weight) / math.pow(float(self.height) / 100, 2), 2)
		
	# returns a list containing lower and upper ideal weight
	def ideal_weight(self):
		ideal_weights = []
		ideal_weights.append(round(math.pow(float(self.height) / 100, 2) * 18.5, 2))
		ideal_weights.append(round(math.pow(float(self.height) / 100, 2) * 25, 2))
		return ideal_weights
	
	# returns list containing: body fat percentage, body fat on body (kg) and body fat percentage category
	def body_fat(self):
		body_fat_list = []
		body_fat_list.append(round((1.20 * self.bmi()) + (0.23 * int(self.age)) - (10.8 * int(self.sex)) - 5.4, 2))
		body_fat_list.append(round(body_fat_list[0] / 100 * float(self.weight), 2))
		if int(self.sex) == 1:
			if body_fat_list[0] > 24:
				body_fat_cat = 'above average'
			elif body_fat_list[0] < 18:
				body_fat_cat = 'below average'
			else:
				body_fat_cat = 'average'
		else:
			if body_fat_list[0] > 31:
				body_fat_cat = 'above average'
			elif body_fat_list[0] < 25:
				body_fat_cat = 'below_average'
			else:
				body_fat_cat = 'average'
		
		body_fat_list.append(body_fat_cat)
		
		return body_fat_list
		
	# returns a positive float of you need to gain weight, returns a negative float if you need to lose weight
	# returns false if no weight change is needed
	def weight_left(self):
		if self.bmi() < 18.5:
			weight_left = self.ideal_weight()[0] - float(self.weight)
			bmi_status = round(weight_left,2)
		elif self.bmi() >= 25:
			weight_left = float(self.weight) - self.ideal_weight()[1]
			bmi_status = round(weight_left,2)
		else:
			bmi_status = False
			
		return bmi_status
		
	def bmi_category(self):
		bmi = self.bmi()
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
			
		return bmi_cat
	
	
