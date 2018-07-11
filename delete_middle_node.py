"""Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node."""

#Time complexity O(N/2)
def delete_middle(list_):
  index = int(len(list_)/2)
  counter = 0
  head = list_.head
  while(head.next):
    counter+=1
    if counter == index:
      head.next = head.next.next
      return
    head = head.next

if __name__ == '__main__':
  list_ = LinkedList()
  list_.generate(10, 0, 30)
  print(list_)
  delete_middle(list_)
  print(list_)
