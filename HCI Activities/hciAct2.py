h = input("Enter height: ")
w = input("Enter width: ")
ctr = 0
while(ctr < int(h)):
	if(ctr==0):
		line = ""
		for num in range (0, int(w), 1):
			line = line + "*   "
		print(line)
	elif(ctr>0 and ctr<int(h)-1):
		line = ""
		for num in range (0,int(w),1):
			if(num==0):
				line = line + "*"
			elif(num==int(w)-1):
				line = line + "*"
			else:
				line = line +"     "
		print(line)
	elif(ctr==int(h)-1):
		line = ""
		for num in range (0, int(w), 1):
			line = line + "*   "
		print(line)
	ctr = ctr + 1