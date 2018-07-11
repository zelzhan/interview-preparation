"""Given two (singly) linked lists, determine if the two lists intersect. Return the inter­
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting."""

#time complexity O(N+K)
def intersection(list1, list2):

  tail1, size1 = tail_and_size(list1)
  tail2, size2 = tail_and_size(list2)
  if tail1 is not tail2: return None
  difference = abs(size1-size2)

  bigger = list1.head if size1 > size2 else list2.head
  smaller = list2.head if size1 > size2 else list1.head

  bigger = cut_off(bigger, difference)
  while bigger is not smaller:
    bigger = bigger.next
    smaller = smaller.next

  return smaller.value
  
def tail_and_size(list_):
  size = 0
  head = list_.head
  while(head.next):
    head = head.next
    size+=1
  return head, size

def cut_off(bigger, difference):
  counter = 0
  while counter != difference:
    counter+=1
    bigger = bigger.next
  return bigger


  
if __name__ == '__main__':
  list1 = LinkedList()
  list2 = LinkedList()
  
  list1.add(1)
  list1.add(2)
  list1.add(3)
  list1.add(4)
  list1.add(5)
  list2.add(5)
  list2.add(19)
  list2.add(22)
  head1, head2 = list1.head, list2.head
  head2.next.next.next = head1.next
  # list1.generate(5, 0, 10)
  # list2.generate(7, 0, 10)
  print(list1)
  print()
  print(list2)
  print(intersection(list1, list2))
