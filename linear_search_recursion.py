# linear search using recursion

def findIndexUsingLinearSearch(array, target, index=0):
	if index == len(array):
		return -1
	if array[index] == target:
		return index
	return findIndexUsingLinearSearch(array, target, index+1)

array = [1, 3, 5, 2, 3, 2]
target = 9
print(findIndexUsingLinearSearch(array, target))
