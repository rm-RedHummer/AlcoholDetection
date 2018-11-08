m = input("Enter mass in kilograms: ")
h = input("Enter height in meters: ")
bmi = float(m)/pow(float(h),2)
if(bmi < 18.5):
	print("You are underweight")
elif(bmi > 18.5 and bmi < 25):
	print("You are normal")
elif(bmi > 25 and bmi < 30):
	print("You are overweight")
elif(bmi > 30):
	print("You are obese")