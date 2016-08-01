# Python port of https://github.com/alizain/ulid
# License MIT
from __future__ import print_function
import os
import sys
import time

ENCODING = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
LENCODING = len(ENCODING)
PY3 = sys.version_info[0] == 3
if PY3:
    long = int
    import codecs
    
def encode_time(x, num):
    s = ''
    while len(s) < num:
        x, i = divmod(x, LENCODING)
        s = ENCODING[i] + s
    return s

def encode_random(num):
    if PY3:
        x = long(codecs.encode(os.urandom(num*LENCODING),'hex'),16)
    else:
        x = long(os.urandom(num*LENCODING).encode('hex'),16)
    s = ''
    while len(s) < num:
        x, i = divmod(x, LENCODING)
        s = ENCODING[i] + s
    return s

def ulid():
    return encode_time(long(time.time()*1000),10)+encode_random(16)

def main():
    for k in range(10):
        print(ulid())

if __name__ == '__main__':
    main()
