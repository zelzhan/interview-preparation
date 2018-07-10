"""Implement a function to check if a linked list is a palindrome."""

#Time complexity O(N)
def palindrome(list_):
  temp_list = LinkedList()
  head = list_.head
  temp_list.add(head.value)
  temp_head = temp_list.head 
  while head.next:
    head = head.next
    temp_list.add(head.value)
    temp_head.next.prev = temp_head
    temp_head = temp_head.next  
  head1 = list_.head
  head2 = temp_head
  counter = 0
  while counter != int(len(list_)/2):
    counter +=1
    if head1.value != head2.value: return False
    head1 = head1.next
    head2 = head2.prev
  return True

if __name__ == '__main__':
  list1 = LinkedList()
  list1.add(1)
  list1.add(2)
  list1.add(3)
  list1.add(4)
  list1.add(3)
  list1.add(2)
  list1.add(1)
  print(list1)
  print(palindrome(list1))
