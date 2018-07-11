""" Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.) """

#time complexity O(N^2)
def solution1(string, length):
    string = string.strip()
    string = string.replace(" ", "%20")
    return string

#time complexity O(N^2)
def solution2(string, length):
    string = string.strip()
    i = 0
    while i < len(string):
        if i == len(string): break
        if string[i] == " ":
            string = string[:i] + "%20" + string[i+1:]
        i+=1
    return string


if __name__ == '__main__':
    string = "hesasdasdk asd aksd kaskd aksdk aksd a   sad jsdf kasjdfk jaksdfj aksjdfk ajsdfk jaskdfj aksjdfff f "
    print(urlfy(string, len(string)))
    print(string)
