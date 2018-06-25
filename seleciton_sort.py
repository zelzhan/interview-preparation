#implementation of selection sort

def selection_sort(arr):
    start = 0
    target = 1
    while arr[start]!=arr[-1]:
        while True:
            if arr[start] > arr[target]:
                temp = arr[start]
                arr[start] = arr[target]
                arr[target] = temp
            target+=1
            if target >= len(arr): break
        start+=1
        target = start+1
    
    
if __name__ == '__main__':
    list_ = [1, 5, 3, 2, 4, 10, 23, 36]
    selection_sort(list_)
    print(list_)
