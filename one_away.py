"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. """

# time complexity O(N^2)
def one_away(string1, string2):
	string1 = list(string1)
	string2 = list(string2)
	num_edits  = abs(len(string1) - len(string2))
	while len(string1) != 0:
		temp = string1.pop()
		if temp in string2:
			string2.remove(temp)
	num_edits += len(string2)
	return True if num_edits < 2 else False



if __name__ == '__main__':
    print(one_away("pale", "bake"))
