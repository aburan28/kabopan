#Tiger Hash
#Cryptographic Hash
#Ross Anderson and Eli Biham, 1996
#Tiger - A Fast New Hash Function
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


import _misc as m
from md4 import *
from _int import QWORD, BYTE, List

#    magic_string = "Tiger - A Fast New Hash Function, by Ross Anderson and Eli Biham"
import tiger_const

class tiger(md4):
    def __init__(self):
        md4.__init__(self)
        self.hv_size = 64

        hex = "0123456789ABCDEF"
        IVhex = hex + hex[::-1]
        self.IVs = QWORDS(list(struct.unpack(">2Q", hex2bin(IVhex)))  + [0xF090A0B0C0B0E080 | 0x0006050403020107])
        self.pad_bit_7 = False

        self.S = tiger_const.Ss_test

        self.sbox = self.S
        self.Sbox = self.S[::-1]
        self.round_indexes = range(0, 8, 2) # even numbers
        self.Round_indexes = range(1, 8, 2) # odd numbers


    def key_schedule(self, words):
          x0, x1, x2, x3, x4, x5, x6, x7 = words

          x0 -= x7 ^ 0xA5A5A5A5A5A5A5A5
          x1 ^= x0
          x2 += x1
          x3 -= x2 ^ ((~x1) << 19)
          x4 ^= x3
          x5 += x4
          x6 -= x5 ^ ((~x4) >> 23)
          x7 ^= x6

          x0 += x7
          x1 -= x0 ^ ((~x7) << 19)
          x2 ^= x1
          x3 += x2
          x4 -= x3 ^ ((~x2) >> 23)
          x5 ^= x4
          x6 += x5
          x7 -= x6 ^ 0x0123456789ABCDEF
          return x0, x1, x2, x3, x4, x5, x6, x7


    def combine(self, bhvs): #: feed forward
        a, b, c = bhvs
        aa, bb, cc = self.ihvs
        a, b, c = [
            a ^ aa,
            b - bb,
            c + cc,
            ]
        return a, b, c


    def round_(self, l, x, mul):
        a, b, c = list(l)
        c ^= x
        ta = m.xor((sbox[c[7 - index]] for sbox, index in zip(self.sbox, self.round_indexes)), QWORD(0))
        tb = m.xor((sbox[c[7 - index]] for sbox, index in zip(self.Sbox, self.Round_indexes)), QWORD(0))
        a -= ta
        b += tb
        b *= mul
        return a, b, c


    def pass_(self, bhvs, mul, words):
        a, b, c = list(bhvs)
        a, b, c = self.round_([a, b, c], words[0], mul)
        b, c, a = self.round_([b, c, a], words[1], mul)
        c, a, b = self.round_([c, a, b], words[2], mul)
        a, b, c = self.round_([a, b, c], words[3], mul)
        b, c, a = self.round_([b, c, a], words[4], mul)
        c, a, b = self.round_([c, a, b], words[5], mul)
        a, b, c = self.round_([a, b, c], words[6], mul)
        b, c, a = self.round_([b, c, a], words[7], mul)
        return a,b,c

    def rounds(self, words):
        a, b, c = list(self.ihvs)
        a ,b, c = self.pass_([a, b, c], 5, words)
        words = self.key_schedule(words)
        c, a, b = self.pass_([c, a, b], 7, words)
        words = self.key_schedule(words)
        b, c, a = self.pass_([b, c, a], 9, words)
        return a, b, c

if __name__ == "__main__":
    import test.tiger_test
