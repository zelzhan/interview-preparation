#implementation of maxHeap and heapsort

class maxHeap:            
    def __init__(self):
        self.size = 0
        self.array = []
        self.root = None        
            
    def heapify(self, list_):
        for i in list_:
            self.insert(i)
        return self.array
    
    def insert(self, value):
        self.array.append(value)
        self.__sift_up()
        
    def get_max(self):
        return self.array[0]
    
    def get_size(self):
        return len(self.array)
    
    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False
    
    def extract_max(self):
        self.__swap(0, len(self.array)-1)
        temp = self.array.pop()
        if len(self.array) > 1:
            self.__sift_down()
        return temp
        
    def remove(self, index):
        self.array.pop(index)
        
    def heap_sort(self, target):
        self.array = self.heapify(target)
        temp = self.array
        res = []
        while (len(self.array) > 0):
            res.insert(0,self.extract_max())
        self.array = temp
        return res
        
    
    def __heap_sort_swap(self, index1, index, arr):
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp
        return arr
        
    def __swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp
            
    def __sift_up(self):
        index = len(self.array)-1
        target = self.array[index]
        while(target > self.array[int((index-1)/2)]):
             self.__swap(index, int((index-1)/2))
             index = int((index-1)/2)
             target = self.array[index]
        
    def __sift_down(self):
        index = 0
        left_child = index*2 + 1
        right_child = index*2 + 2
        
        if len(self.array) == 2:
            if self.array[left_child] > self.array[index]:
                self.__swap(left_child, right_child)
            return
            
        maxi = left_child if self.array[left_child] > self.array[right_child] else right_child
        while(self.array[index] < self.array[maxi]):
            self.__swap(index, maxi)
            left_child = index*2 + 1
            right_child = index*2 + 2
            maxi = left_child if self.array[left_child] > self.array[right_child] else right_child
            if maxi > len(self.array): 
                return

    
if __name__ == '__main__':
    heap = maxHeap()

    list_ = [0, 5, 7, 2, 3, 10, 15]
    print(heap.heap_sort(list_))
