#implementation of maxHeap

class maxHeap:            
    def __init__(self):
        self.size = 0
        self.array = []
        self.root = None
        
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
        print(self.array)
        
    def __sift_down(self):
        index = 0
        left_child = index*2 + 1
        right_child = index*2 + 2
        
        if len(self.array) == 2:
            if self.array[left_child] > self.array[index]:
                self.__swap(left_child, right_child)
            return
        
       # if len(self.array) == 3:
            
        maxi = left_child if self.array[left_child] > self.array[right_child] else right_child
        while(self.array[index] < self.array[maxi]):
            self.__swap(index, maxi)
            left_child = index*2 + 1
            right_child = index*2 + 2
            maxi = left_child if self.array[left_child] > self.array[right_child] else right_child
            if maxi > len(self.array): 
                return
        
            
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
        print(self.array)
        return temp
        
    def remove(index):
        self.array.pop(index)

    
if __name__ == '__main__':
    heap = maxHeap()
    heap.insert(1)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    heap.insert(5)
    heap.insert(10)
    heap.insert(111)
    heap.insert(12)
    heap.insert(1122)
    heap.insert(13)
    for i in range(0, 20):
        heap.insert(i)
    heap.extract_max()
    heap.extract_max()
    heap.extract_max()
    
    heap.extract_max()
    print(heap.extract_max())
    
     
        
