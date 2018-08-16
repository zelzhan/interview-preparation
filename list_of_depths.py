"""Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)."""
class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def list_of_depths(root):
  res = []
  result = []
  res.append([root])
  helper(res, [root])
  for i in res:
    result.append([x.data for x in i])
  return result
  

def helper(res,tempList):
  myList = []
  for i in tempList:
    if i.left:
      myList.append(i.left)
    if i.right:
      myList.append(i.right)
  if len(myList) == 0:
    return
  res.append(myList)
  helper(res, myList)


if __name__ == '__main__':
  #list_of_depths()

# Use the insert method to add nodes
  root = Node(12)
  root.insert(6)
  root.insert(14)
  root.insert(3)
  root.insert(4)
  root.insert(2)

  root.PrintTree()
  print(list_of_depths(root))
