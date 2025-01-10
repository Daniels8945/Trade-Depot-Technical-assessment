import sys

if __name__ == "__main__":
    """ Take's a string as input and
        return the reversed string"""
    argc = sys.argv[1]
    for i,j in enumerate(argc):
        wrd = argc[-1-i]
        print('{:s}'.format(wrd), end='')