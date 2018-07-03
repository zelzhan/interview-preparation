"""Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. """

#Time complexity O(N^2)

def palindrome(string):
	center = ""
	string = list(string.replace(" ", "").lower())
	while len(string) != 0:
		temp = string.pop()
		if temp not in string and center != "":
			return False
		elif temp not in string:
			center = temp
		else:
			string.remove(temp)
	return True


if __name__ == '__main__':
    string = "hesasdasdk asd aksd kaskd aksdk aksd a   sad jsdf kasjdfk jaksdfj aksjdfk ajsdfk jaskdfj aksjdfff f "
    string2 = "Tact Coa"
    string3 = "shaAshl"
    print(palindrome(string2))
    print(palindrome(string))
    print(palindrome(string3))
