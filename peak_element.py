
#simple linear scan
#O(N)
def maxima1(some_list):
  res = []
  for i in range(len(some_list)):
    if i == len(some_list) -1: 
      if some_list[i] > some_list[i-1]:
        res.append(some_list[i])
      break
    if i != 0 and some_list[i] > some_list[i+1] and some_list[i] > some_list[i-1]:
      res.append(some_list[i])
  return res

#recursive implementation
#O(logN)
def maxima(some_list):
	return finder(int(len(some_list)/2), 0, len(some_list) -1, some_list)

def finder(mid, left, right, some_list):
	#rightmost case
  if some_list[mid] == some_list[len(some_list) - 1]:
    
    return some_list[mid]

  #leftmost case
  if some_list[mid] == some_list[0]: 
    
    return some_list[mid]
	
	#check for maxima
  if some_list[mid] >= some_list[left] and some_list[mid] >= some_list[right]: 
    return some_list[mid]
	
  if some_list[mid] < some_list[mid+1]:
    mid = left + (right-left)/2
    left = mid + 1
    return finder(mid, left, right, some_list)
  else: 
    mid = left + (right-left)/2
    right = mid - 1
    return finder(mid, left, right, some_list)


if __name__ == '__main__':
  list_ = [100, 80, 60, 50, 20]
  print(maxima(list_))
