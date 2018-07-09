"""Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?"""

#O(N^2)
from LinkedList import LinkedList
def remove_duplicates(list_):
  head = list_.head
  while head.next:
    temp = head.value
    temp_head = head
    while temp_head.next:
      if temp_head.next.value == temp:
        temp_head.next = temp_head.next.next
      else:
        temp_head = temp_head.next
      if head == None: break    
    head = head.next
    if head == None: break
  return list_


if __name__ == '__main__':
  list_ = LinkedList()
  list_.generate(40, 0, 8)
  print(list_)
  list_ = remove_duplicates(list_)
  print(list_)
