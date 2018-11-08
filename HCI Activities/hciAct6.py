name_list = ['Kerby', 'Reina', 'Simon', 'Roy', 'Eve', 'Mavic', 'Pen', 'Linda', 'John', 'Brandi' ]
innum = 0
sum = 0
for num in range (0,len(name_list)): #10
	if num < len(name_list)-1:
		innum = num+1
	while innum < len(name_list):
		print (name_list[num],name_list[innum])
		innum = innum+1
		sum = sum + 1
print ( "There are "+ str(sum) + " partnerships")
