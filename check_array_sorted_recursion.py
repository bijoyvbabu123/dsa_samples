# to check if the array is sorted in ascending order using recursion

def check_if_sorted(array,pointer=0):
	if pointer == len(array)-1:
		return True
	return array[pointer] < array[pointer+1] and check_if_sorted(array, pointer+1)



# array = [1, 2, 3, 4, 5]
array = [1, 3, 5, 2, 3]
print(check_if_sorted(array))
