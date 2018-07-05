"""Assumeyou have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")."""

#Time complexity O(N^2)
def string_rotation(string1, string2):
  i = 0
  j = 0
  if len(string1) != len(string2): return False
  while i != len(string1): 
    if string1[i] == string2[0]:
      temp = i
      while j != len(string1):
        if string1[i] != string2[j]:
          break
        if j+1 == len(string2):
          return True
        i+=1
        j+=1
        if i == len(string1): i = 0
      i = temp
      j = 0
    i+=1
  return False

if __name__ == '__main__':
  str1 = "hello"
  str2 = "lohel"
  print(string_rotation(str1, str2))
