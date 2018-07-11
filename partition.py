"""Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions."""


def partition(list1, x):
  list2 = LinkedList()

  head = list1.head
  if head.value < x: list2.add(head.value)
  while head.next:
    head = head.next
    if head.value < x: list2.add(head.value)

  head = list1.head
  if head.value >= x: list2.add(head.value)
  while head.next:
    head = head.next
    if head.value >= x: list2.add(head.value)
  
  return list2

  
if __name__ == '__main__':
  list1 = LinkedList()
  list2 = LinkedList()

  list1.generate(30, 0, 10)
  # list2.generate(7, 0, 10)
  print(list1)
  print()
  # print(list2)
  print(partition(list1, 5))
