#Secure Hash Algorithm 2 - SHA-2, SHA256
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


from sha256 import *
from _int import Int, DWORDS
from _sha2 import nroot_primes

class sha224(sha256):
    def __init__(self):
        sha256.__init__(self)
        self.IVs = DWORDS(nroot_primes(8, 16, 2, 64)) #:Lowest 32 bits of sha384 IVs

    def digest(self):
        return sha256.digest(self)[:28]


if __name__ == "__main__":
    import sha224_test
