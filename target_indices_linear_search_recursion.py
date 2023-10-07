# find the list of indices containing the target element in a list using recursion

def findListOfIndicesOfTarget(array, target, index=0):
	indices = list()
	# print(index, array, indices)
	if index == len(array):
		return indices
	if array[index] == target:
		indices.append(index)
	# print(index, array, indices)
	indices.extend(findListOfIndicesOfTarget(array, target, index+1))
	# print(index, array, indices)	
	return indices

array = [1, 2, 3, 2]
target = 2
print(findListOfIndicesOfTarget(array, target))
