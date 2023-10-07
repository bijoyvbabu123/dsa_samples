# given a string, remove character 'a' from it and print the new string

def removeCharacterA(s, index=0):
	if index == len(s):
		return ""
	if s[index] != 'a':
		return  s[index] + removeCharacterA(s, index+1)
	return removeCharacterA(s, index+1)

def removeCharacterA_(p, up):
	if up == "":
		return p
	if up[0] == 'a':
		return removeCharacterA_(p, up[1:])
	return removeCharacterA_(p+up[0], up[1:])


s = "banana"
print(removeCharacterA(s))
print(removeCharacterA_("", s))
