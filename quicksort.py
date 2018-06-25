#implementation of quicksort

def quick_sort(arr):
    quick_sort_helper2(arr, 0, len(arr)-1)
  
def swap(index1, index2, arr):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
        
    
def quick_sort_helper2(arr, left, right):
    if left > right: return
    templeft = left
    tempright = right
    pivot = arr[left]
    while True:
        while arr[right] > pivot:
            right-=1
        while arr[left] < pivot:
            left+=1
        swap(left, right, arr)
        if right <= left: break
    quick_sort_helper2(arr, left + 1, tempright)
    quick_sort_helper2(arr, templeft, left-1)




if __name__ == '__main__':
    list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    test1 = [0, 2, 5, 3, 4, 10, 16, 202, 8]
    test = [3, 2, 11, 1, 22, 0]
    
    quick_sort(test)
    print(test)
