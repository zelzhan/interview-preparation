"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. """

# time complexity O(N)
def one_away(stringg1, stringg2):
  string1 = list(stringg1)
  string2 = list(stringg2)
  num_edits1  = abs(len(string1) - len(string2))
  while len(string1) != 0:
    temp1 = string1.pop()
    if len(string2) != 0:
      temp2 = string2.pop()
      if temp1 != temp2: num_edits1+=1
  

  string1 = list(stringg1)[::-1]
  string2 = list(stringg2)[::-1]
  num_edits2  = abs(len(string1) - len(string2))
  while len(string1) != 0:
    temp1 = string1.pop()
    if len(string2) != 0:
      temp2 = string2.pop()
      if temp1 != temp2: num_edits2+=1
  
  return True if num_edits1 < 2 or num_edits2 < 2 else False
    

if __name__ == '__main__':
    print(one_away("apale", "pale"))

