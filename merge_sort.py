#implementation of merge sort

def merge(arr1, arr2):
    res = []
    while(True):
        temp1 = arr1.pop(0)
        temp2 = arr2.pop(0)
        if temp1 < temp2:
            res.append(temp1)
            arr2.insert(0, temp2)
        else:
            res.append(temp2)
            arr1.insert(0, temp1)
        if len(arr1) == 0 :
            while(len(arr2) != 0): res.append(arr2.pop(0))
            break
        if len(arr2) == 0 :
            while(len(arr1) != 0): res.append(arr1.pop(0))
            break
    return res     
        
    
def merge_sort(arr1):
    if len(arr1) == 1: return arr1
    temp = int(len(arr1))
    arr2 = []
    
    while(len(arr1) != int(temp/2)):
        arr2.append(arr1.pop())   
        
    temp1 = merge_sort(arr1)
    temp2 = merge_sort(arr2)
    return merge(temp1, temp2)
     

if __name__ == '__main__':
    list_ = [3, 5, 1, 2, 10, 15, 4, 0]
    list2 = []
    
    for j in range(50000, 0, -1):
        list2.append(j)
    
    #print(list2)
    print(merge_sort(list2))
