"""Given a sequence of brackets, how will you identify if its valid or not."""

def valid(brackets):
  if len(brackets) % 2 != 0: return False
  length = len(brackets)
  checker = []
  temp = ''
  dictn = {'}':'{', '[':']', '(':')', '{':'}', ']':'[', ')':'('}
  while len(brackets) != 0:
    if len(checker) != 0: temp = checker.pop()
    bracket = brackets.pop()
    if dictn[bracket] != temp and temp != '': 
      checker.append(temp)
      checker.append(bracket)
		
  if len(checker) == 0: return True
  print(checker)
  return False


if __name__ == '__main__':
  list_ = ['(', '{','[',']',']','}', ')' ]
  print(valid(list_))
