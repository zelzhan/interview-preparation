def compression(string):
	if len(string) <= len(set(string))*2: return string
	temp_set = list(set(string))
	list_ = []
	for i in range(len(temp_set)):
		temp_var = temp_set.pop()
		counter = 0
		for j in string:
			if j == temp_var: counter+=1
		list_.append(temp_var)
		list_.append(str(counter))
	return "".join(list_)



if __name__ == '__main__':
    print(compression("aabbsccc"))
