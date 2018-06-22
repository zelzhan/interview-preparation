#implementation of insertion sort

def insertion_sort(arr):
    for i in range(len(arr)-1):
        index = i
        while arr[index] > arr[index+1]:
            temp = arr[index+1]
            arr[index+1] = arr[index]
            arr[index] = temp
            index-=1
            if index == -1: break
            print(arr)
    return arr

            
if __name__ == '__main__':
    list_ = [3, 5, 1, 2, 10, 15, 4, 0]
    print(insertion_sort(list_))
