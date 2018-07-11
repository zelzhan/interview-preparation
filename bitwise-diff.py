#Write a function to count the number of bits that are different between two numbers

def bitwise(var1, var2):
    mask = var1 ^ var2
    counter = 0
    while(mask!=0):
        counter += mask & 1 
        mask = mask >> 1
    return counter

if __name__ == '__main__':
    print(count(88, 122))
