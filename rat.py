import sys
from random import randint

def rat(f, n):
    jump = n
    inp = open(f,'r')
    message = inp.read()
    cyphertext = ""
    for letter in message:
        cyphertext += chr((ord(letter.lower()) +  jump - 97) % 26 + 97) if (97 <= ord(letter.lower()) < 123) else letter
    return cyphertext



print rat(sys.argv[1],randint(1,25))
print 
