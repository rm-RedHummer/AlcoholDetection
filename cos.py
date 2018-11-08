import math
from sympy import *
x, y, z = symbols ('x y z')
init_printing(use_unicode=True)
while (True):
	print ("Please select from the following:\n1. Cosine\n2. Sine\n3. Tangent\n4. X and Y\n5. Torque\n6. Kinetic Energy\n7. Derivative of Cosine\n8. Integral of Sine")
	select = input()
	if select == "1":
		print("Please select what you want to find\n1. Degree\n2. Horizontal Axis\n3. Inclined Axis")
		cosineSelect = input()
		if cosineSelect == "1":
			print("Enter Horizontal Axis")
			horizontalAxis = input()
			print("Enter Inclined Axis")
			inclinedAxis = input()
			degrees = math.acos(float(horizontalAxis)/float(inclinedAxis))
			print ("The degrees is",degrees*100)
		elif cosineSelect == "2":
			print("Enter degrees")
			degrees = input()
			print("Enter Inclined Axis")
			inclinedAxis = input()
			horizontalAxis = math.cos(float(degrees)*.01)*float(inclinedAxis)
			print("The horizontal axis is",horizontalAxis)
		elif cosineSelect == "3":
			print("Enter Degrees")
			degrees = input()
			print("Enter Horizontal Axis")
			horizontalAxis = input()
			inclinedAxis = float(horizontalAxis)/math.cos(float(degrees)*.01)
			print("The inclined axis is",inclinedAxis)
	elif select == "2":
		print("Please select what you want to find\n1. Degree\n2. Vertical Axis\n3. Inclined Axis")
		sineSelect = input()
		if sineSelect == "1":
			print("Enter Vertical Axis")
			verticalAxis = input()
			print("Enter Inclined Axis")
			inclinedAxis = input()
			degrees = math.asin(float(verticalAxis)/float(inclinedAxis))
			print ("The degrees is",degrees*100)
		elif sineSelect == "2":
			print("Enter degrees")
			degrees = input()
			print("Enter Inclined Axis")
			inclinedAxis = input()
			verticalAxis = math.sin(float(degrees)*.01)*float(inclinedAxis)
			print("The vertical axis is",verticalAxis)
		elif sineSelect == "3":
			print("Enter Degrees")
			degrees = input()
			print("Enter Vertical Axis")
			verticalAxis = input()
			inclinedAxis = float(verticalAxis)/math.sin(float(degrees)*.01)
			print("The inclined axis is",inclinedAxis)
	elif select == "3":
		print("Please select what you want to find\n1. Degree\n2. Vertical Axis\n3. Horizontal Axis")
		sineSelect = input()
		if sineSelect == "1":
			print("Enter Vertical Axis")
			verticalAxis = input()
			print("Enter Horizontal Axis")
			horizontalAxis = input()
			degrees = math.atan(float(verticalAxis)/float(horizontalAxis))
			print ("The degrees is",degrees*100)
		elif sineSelect == "2":
			print("Enter degrees")
			degrees = input()
			print("Enter Horizontal Axis")
			horizontalAxis = input()
			verticalAxis = math.tan(float(degrees)*.01)*float(horizontalAxis)
			print("The vertical axis is",verticalAxis)
		elif sineSelect == "3":
			print("Enter Degrees")
			degrees = input()
			print("Enter Vertical Axis")
			verticalAxis = input()
			horizontalAxis = float(verticalAxis)/math.tan(float(degrees)*.01)
			print("The horizontal axis is",horizontalAxis)
	elif select == "4":
		print("Enter 1st equation")
		input1 = input()
		equation1 = list(input1)
		print("Enter 2nd equation")
		input2 = input()
		equation2 = list(input2)

		e1x = ""
		e1y = ""
		e1ans = ""
		for index in range(len(equation1)):
			if equation1[index] == "x":
				for xIndex in range(index):
					e1x = e1x + equation1[xIndex]
			elif equation1[index] == "y":
				yIndex = index-1
				while (yIndex>1):
					if equation1[yIndex]!="+" and equation1[yIndex]!="/" and equation1[yIndex]!="*":
						e1y = equation1[yIndex]+e1y
						if equation1[yIndex]=="-":
							yIndex = 1
					else:
						yIndex = 1
					yIndex = yIndex-1
			elif equation1[index] == "=":
				ansIndex = index+1
				while (ansIndex<len(equation1)):
					e1ans = e1ans + equation1[ansIndex]
					ansIndex = ansIndex + 1
		e2x = ""
		e2y = ""
		e2ans = ""
		for index in range(len(equation2)):
			if equation2[index] == "x":
				for xIndex in range(index):
					e2x = e2x + equation2[xIndex]
			elif equation2[index] == "y":
				yIndex = index-1
				while (yIndex>1):
					if equation2[yIndex]!="+" and equation2[yIndex]!="/" and equation2[yIndex]!="*":
						e2y = equation2[yIndex]+e2y
						if equation2[yIndex]=="-":
							yIndex = 1
					else:
						yIndex = 1
					yIndex = yIndex-1
			elif equation2[index] == "=":
				ansIndex = index+1
				while (ansIndex<len(equation2)):
					e2ans = e2ans + equation2[ansIndex]
					ansIndex = ansIndex + 1

		print(str(e2x))
		e1x2 = float(e1x)
		e1y2 = float(e1y)
		e1ans2 = float(e1ans)

		e2x2 = float(e2x)
		e2y2 = float(e2y)
		e2ans2 = float(e2ans)

		e1x=e1x2
		e1y=e1y2
		e1ans=e1ans2
		e2x=e2x2
		e2y=e2y2
		e2ans=e2ans2

		y = 0
		x = 0
		if e1x+e2x == 0:
			y = (e1ans+e2ans)/(e1y+e2y)
		elif e1y+e2y == 0:
			x = (e1ans+e2ans)/(e1x+e2x)

		if e1x>0 and e2x>0 :
			negative = e2x*-1
			e1yTemp = negative*e1y
			e1ansTemp = negative*e1ans

			e2yTemp = e1x*e2y
			e2ansTemp = e1x*e2ans

			yTemp = e1yTemp+e2yTemp
			ansTemp = e1ansTemp + e2ansTemp

			if yTemp!=1:
				y = ansTemp/yTemp
			else:
				y = ansTemp

		print("The value of X is", x)
		print("The value of Y is", y)

		#print (str(e1x) + " " + e1y + " " + e1ans + " " + e2x + " " + e2y + " " + e2ans)

	elif select == "5":
		print("Enter distance")
		distance = float(input())
		print("Enter force")
		force = float(input())
		torque = distance*force
		print("The computed torque is",torque)
	elif select == "6":
		print("Enter mass")
		mass = float(input())
		print("Enter velocity")
		velocity = float(input())
		kineticEnergy = ((velocity**2)*mass)/2
		print("The computed kinetic energy is",kineticEnergy)
	elif select == "7":
		print("Enter value of x")
		val = input()
		print("The derivative of",val,"is",diff(cos(val),x))

	elif select == "8":
		print("Enter value of x")
		val = input()
		print("The integral of",val,"is",integrate(sin(val),x))
