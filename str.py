import sys

if __name__ == "__main__":
    """ Take a string as input 
        return the reversed string"""
    argc = sys.argv[1]
    for i,n in enumerate(argc):
        wrd = argc[-1-i]
        print('{:s}'.format(wrd), end='')