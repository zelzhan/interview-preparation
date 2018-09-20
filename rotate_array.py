#The following code is supposed to rotate the array A by B positions.

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    
    def append_right_hand(self, ret, a, b):
        counter = 0
        while counter != b:
            ret.append(a[counter])
            counter +=1
        print(ret)
            
    def rotateArray(self, a, b):
        ret = []
        for i in range(len(a)):
            print(i+b)
            print(len(a))
            print(ret)
            print()
            if i+b == len(a):
                self.append_right_hand(ret, a, b)
                break
            ret.append(a[i + b])
        return ret
        
        
if __name__ == '__main__':
  sol = Solution()
  print(sol.rotateArray([1, 2, 3, 4, 5], 1))
            
