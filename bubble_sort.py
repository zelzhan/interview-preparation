#implementation of bubble sort

def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr


if __name__ == '__main__':
    list_ = [1, 3, 5, 2, 10, 15, 4, 0]
    print(bubble_sort(list_))
