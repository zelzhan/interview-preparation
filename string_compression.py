"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). """

#Time complexity = O(N^2)
def compression(string):
	if len(string) <= len(set(string))*2: return string 	#O(1) + O(N) + O(1) = O(N)
	temp_set = list(set(string))				#O(N) + O(N) =  O(N)    each type conversion takes O(N)
	list_ = []
	for i in range(len(temp_set)):				#O(N^2) terrible
		temp_var = temp_set.pop()				
		counter = 0		
		for j in string:					
			if j == temp_var: counter+=1			
		list_.append(temp_var)
		list_.append(str(counter))
	return "".join(list_)

								

if __name__ == '__main__':
    print(compression("aabbsccc"))
