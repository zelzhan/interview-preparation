"""You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list."""

def sum_lists(list1, list2):
  head1 = list1.head
  head2 = list2.head
  li = LinkedList()
  next_value = 0
  while(head1.next and head2.next):
    li.add(((head1.value + head2.value) % 10) + next_value)
    next_value = (head1.value + head2.value) // 10
    head1 = head1.next
    head2 = head2.next
    if head1.next == None and head2.next != None:
      while head2.next:
        li.add(head2.value+next_value)
        head2 = head2.next
        next_value = 0
    elif head2.next == None and head1.next != None:
      while head1.next:
        li.add(head1.value+next_value)
        head1 = head1.next
        next_value = 0
    elif head2.next or head1.next:
      li.add(((head1.value + head2.value) % 10) + next_value)
  return li





if __name__ == '__main__':
  list1 = LinkedList()
  list2 = LinkedList()
  list1.generate(3, 0, 10)
  list2.generate(3, 0, 10)
  print(list1)
  print(list2)
  print(sum_lists(list1, list2))
