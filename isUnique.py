"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? """

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
