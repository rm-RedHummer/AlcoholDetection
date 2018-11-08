X_list = [11, 6, 5, 7, 10]
new_list=[]
for num in X_list:
	if num%2 == 0 :
		new_list.append(num+1)
		continue
	new_list.append(num)
print(new_list)