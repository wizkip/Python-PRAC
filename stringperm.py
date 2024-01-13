#Lets do a simple program to print out the PERMUTATIONS of AWS

from itertools import permutations

def permstr(str):

    permlist = permutations(str)

    for perm in list(permlist):

        print(''.join(perm))

if __name__ == "__main__":

    str = "AWS"
    permstr(str)
    #the Beautiful PERMUTATIONS



