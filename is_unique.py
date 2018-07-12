"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? """


#Time complexity O(N). Trivial solution
def checker(string)
    set_of_char = set(string)
    return True if len(set_of_char) == len(string) else False

#time complexity O(N^2)
def checker(string):
    while string != "":
        temp = string[0]
        string = string[1:]
        if temp in string:
            return True
    return False

if __name__ == '__main__':
    print(checker("hesl"))
