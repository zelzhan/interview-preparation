class Node():
    value = None
    right = None
    left = None
    
    def __init__(self, value):
        self.value = value
        
        
class BST():
        
    def __init__(self):
        self.size = 0
        self.root = None
        
    def insert(self, value):
        temp = root
        while(temp != None):
            if value > temp.value:
                temp = temp.left
            elif value < temp.value:
                temp = temp.right
        temp.
        
            
            


if __name__ == '__main__':
    bst = BST()
    print(bst.insert(11))
    print(bst.root.value)
