# find all the subsets of the list of numbers

def printSubsets(p, up):
	if len(up) == 0:
		print(p)
		return
	new_up = up[1:]
	new_p = p.copy()
	printSubsets(new_p, new_up)
	_p = p.copy()
	_p.append(up[0])
	printSubsets(_p, new_up)

def listOfSubsets(p, up):
	if not up:
		return [p]

	subset_list = list()

	curr_num = up[0]

	new_up = up[1:]

	_p = p.copy()
	subset_list.extend(listOfSubsets(_p, new_up))

	__p = p.copy()
	__p.append(curr_num)
	subset_list.extend(listOfSubsets(__p, new_up))

	return subset_list

def listOfSubsetsWithoutListCopy(p, up):
	if not up:
		pp = p.copy()
		return [pp]
	
	subset_list = list()
	curr_num = up[0]

	p.append(curr_num)
	subset_list.extend(listOfSubsetsWithoutListCopy(p, up[1:]))
	if p:
		p.pop(-1)
	subset_list.extend(listOfSubsetsWithoutListCopy(p, up[1:]))
	return subset_list





nums = [2, 3, 4]
l = list()
# printSubsets(l, nums)
# print(listOfSubsets(l, nums))
print(listOfSubsetsWithoutListCopy(l, nums))
