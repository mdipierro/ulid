# Python port of https://github.com/alizain/ulid
# https://github.com/mdipierro/ulid
# License MIT
from __future__ import print_function
import os
import sys
import time
import codecs

ENCODING = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
LENCODING = len(ENCODING)


PY3 = sys.version_info[0] == 3
    
def encode_time_10bytes(x):
    s = ''
    while len(s) < 10:
        x, i = divmod(x, LENCODING)
        s = ENCODING[i] + s
    return s

def encode_random_16bytes():
    b = os.urandom(10)
    x = int(codecs.encode(b, 'hex') if PY3 else b.encode('hex'), 16)
    s = ''
    while len(s) < 16:
        x, i = divmod(x, LENCODING)
        s = ENCODING[i] + s
    return s

def convert(chars):
    i = 0
    n = len(chars)-1
    for k, c in enumerate(chars):
        i = i + 32**(n-k) * ENCODING.index(c)
    return i

def seconds(ulid):
    """ return the timestamp from a ulid """
    return 0.001*convert(ulid[:10])

def sharding(ulid, partitions):
    """ return a sharting partition where to store the ulid"""
    return convert(ulid[-16:]) % partitions

def ulid():
    return encode_time_10bytes(int(time.time()*1000)) + encode_random_16bytes()

def main():
    for _ in range(10):
        print(ulid())

if __name__ == '__main__':
    main()
