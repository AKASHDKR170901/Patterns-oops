def findThreeLargestNumbers(array):
    threelargest=[None,None,None]
    for num in array:
        updatelargest(threelargest,num)
	return threelargest
def updatelargest(threelargest,num):
	if threelargest[2] is None or num>threelargest[2]:
		shiftupdate(threelargest,num,2)
	elif threelargest[1] is None or num>threelargest[1]:
		shiftupdate(threelargest,num,1)
	elif threelargest[0] is None or num>threelargest[0]:
		shiftupdate(threelargest,num,0)
def shiftupdate(array,num,idx):
	for i in range(idx+1):
		if i==idx:
			array[i]=num
		else:
			array[i]=array[i+1]