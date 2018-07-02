""" Given two strings, write a method to decide if one is a permutation of the
other. """

def checker(string1, string2):
	string1 = list(string1)
	string2 = list(string2)
	if len(string1) != len(string2):
		return False
	for i in range(len(string1)):
		temp = string1.pop()
		if temp not in string2:
			return False
		string2.remove(temp)
	return True


if __name__ == '__main__':
    print(checker("hesl", "lseh"))
