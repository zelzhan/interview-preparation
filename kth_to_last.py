"""Implement an algorithm to find the kth to last element of a singly linked list."""

#Time complexity O(N)
def return_kth_to_last(list_, k):
  length = 0
  head = list_.head
  while(head.next):
    length+=1
    head = head.next
  counter = 0
  head = list_.head
  while(head.next):
    counter +=1
    head = head.next
    if counter == length-k+1:
      return head.value
  return -1

if __name__ == '__main__':
  list_ = LinkedList()
  list_.generate(40, 0, 30)
  print(list_)
  print(return_kth_to_last(list_, 5))
