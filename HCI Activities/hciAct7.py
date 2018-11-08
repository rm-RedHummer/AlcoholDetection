num = raw_input("Enter a 9 digit integer: ")
numList = list(num)
sum = 0
for num in range(1,len(numList)+1):
	sum = sum + (int(numList[num-1])*num)
if sum%11 == 10:
	numList.append("X")
else:
	numList.append(sum%11)
numList.insert(1,"-")
numList.insert(5,"-")
numList.insert(11,"-")
output=""
for num in numList:
	output = output + str(num)


print output