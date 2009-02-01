#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

"""tiger2 is tiger, with sha-like padding (big-endian) instead of md4-like padding"""

import tiger

def hash(message):
    return tiger.hash(message, tiger2=True)

def hexhash(message):
    return tiger.hexhash(message, tiger2=True)

if __name__ == "__main__":
    import tiger2_test