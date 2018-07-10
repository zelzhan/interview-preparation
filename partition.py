"""Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions."""



def partition(list_, x):
  #TODO size less than 3
  left = list_.head
  mid = left.next
  right = mid.next
  while(right.next):
    if right.next.value > x:

      left.next = right
      temp = right.next
      right.next = mid
      
      temp_mid = right
      while(temp_mid.next != mid):
        temp_mid = temp_mid.next
      temp_mid.next = temp

      #reassign references
      mid = right
      right = temp_mid
      print()
      print(list_)
      print()
    right = right.next

    




if __name__ == '__main__':
  list_ = LinkedList()
  list_.generate(20, 0, 7)
  print(list_)
  partition(list_, 4)
  print()
  print(list_)
