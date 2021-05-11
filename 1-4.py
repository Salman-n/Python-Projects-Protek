import numpy as np

def createArray():
	global list
	list = np.array([1,1,2,3,4,5])
	print(list);

def appendArray():
	global lists
	lists = np.append(list,[6])
	print(lists);

def reverseArray():
	list = np.flip(lists)
	print(list);

def occurenceArray(num):
	count = np.count_nonzero(list == num)
	print("There is " + str(count) + " occurence of " + str(num));
 
print("1.Create Array")
createArray()
print("2.Append Array")
appendArray()
print("3.Reverse Array")
reverseArray()
print("4.Array Occurence")
print(list)
occurenceArray(1)
occurenceArray(2)
