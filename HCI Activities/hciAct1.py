upper = input("Enter upper limit: ")
lower = input("Enter lower limit: ")
output = 0
for a in range(int(lower),int(upper)+1,1):
	output = output + a
print("The sum within the range is "+str(output))