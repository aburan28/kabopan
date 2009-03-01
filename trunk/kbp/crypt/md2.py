#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
MD2 - Message Digest 2

Cryptographic hash
The MD2 Message-Digest Algorithm
B. Kaliski, 1992
"""

from kbp._misc import as_bytes_blocks
from kbp.types import bytes, Byte, Utility
from kbp.crypt.Hash import Merkledamgaard

class Md2_u(Utility):
    """utility class for MD2 cryptographic hash"""
    pi_subst = [ # how to calculate this ?
     0x29, 0x2e, 0x43, 0xc9, 0xa2, 0xd8, 0x7c, 0x01,
     0x3d, 0x36, 0x54, 0xa1, 0xec, 0xf0, 0x06, 0x13,
     0x62, 0xa7, 0x05, 0xf3, 0xc0, 0xc7, 0x73, 0x8c,
     0x98, 0x93, 0x2b, 0xd9, 0xbc, 0x4c, 0x82, 0xca,
     0x1e, 0x9b, 0x57, 0x3c, 0xfd, 0xd4, 0xe0, 0x16,
     0x67, 0x42, 0x6f, 0x18, 0x8a, 0x17, 0xe5, 0x12,
     0xbe, 0x4e, 0xc4, 0xd6, 0xda, 0x9e, 0xde, 0x49,
     0xa0, 0xfb, 0xf5, 0x8e, 0xbb, 0x2f, 0xee, 0x7a,
     0xa9, 0x68, 0x79, 0x91, 0x15, 0xb2, 0x07, 0x3f,
     0x94, 0xc2, 0x10, 0x89, 0x0b, 0x22, 0x5f, 0x21,
     0x80, 0x7f, 0x5d, 0x9a, 0x5a, 0x90, 0x32, 0x27,
     0x35, 0x3e, 0xcc, 0xe7, 0xbf, 0xf7, 0x97, 0x03,
     0xff, 0x19, 0x30, 0xb3, 0x48, 0xa5, 0xb5, 0xd1,
     0xd7, 0x5e, 0x92, 0x2a, 0xac, 0x56, 0xaa, 0xc6,
     0x4f, 0xb8, 0x38, 0xd2, 0x96, 0xa4, 0x7d, 0xb6,
     0x76, 0xfc, 0x6b, 0xe2, 0x9c, 0x74, 0x04, 0xf1,
     0x45, 0x9d, 0x70, 0x59, 0x64, 0x71, 0x87, 0x20,
     0x86, 0x5b, 0xcf, 0x65, 0xe6, 0x2d, 0xa8, 0x02,
     0x1b, 0x60, 0x25, 0xad, 0xae, 0xb0, 0xb9, 0xf6,
     0x1c, 0x46, 0x61, 0x69, 0x34, 0x40, 0x7e, 0x0f,
     0x55, 0x47, 0xa3, 0x23, 0xdd, 0x51, 0xaf, 0x3a,
     0xc3, 0x5c, 0xf9, 0xce, 0xba, 0xc5, 0xea, 0x26,
     0x2c, 0x53, 0x0d, 0x6e, 0x85, 0x28, 0x84, 0x09,
     0xd3, 0xdf, 0xcd, 0xf4, 0x41, 0x81, 0x4d, 0x52,
     0x6a, 0xdc, 0x37, 0xc8, 0x6c, 0xc1, 0xab, 0xfa,
     0x24, 0xe1, 0x7b, 0x08, 0x0c, 0xbd, 0xb1, 0x4a,
     0x78, 0x88, 0x95, 0x8b, 0xe3, 0x63, 0xe8, 0x6d,
     0xe9, 0xcb, 0xd5, 0xfe, 0x3b, 0x00, 0x1d, 0x39,
     0xf2, 0xef, 0xb7, 0x0e, 0x66, 0x58, 0xd0, 0xe4,
     0xa6, 0x77, 0x72, 0xf8, 0xeb, 0x75, 0x4b, 0x0a,
     0x31, 0x44, 0x50, 0xb4, 0x8f, 0xed, 0x1f, 0x1a,
     0xdb, 0x99, 0x8d, 0x33, 0x9f, 0x11, 0x83, 0x14]

    @staticmethod
    def padpkcs7(length):
        #todo : merge with Pad, pkcs7 modulo 16 ?
        modulo_16 = ((16 - length) % 16)
        padding = modulo_16 if modulo_16 > 0 else 16
        padding_string = chr(padding) * padding
        return padding_string

    @staticmethod
    def checksum(message):
        checksum_bytes = [0 for i in xrange(16)]
        previous = 0
        for block in as_bytes_blocks(message, 16):
            for i, char in enumerate(block):
                # careful, RFC1319 is wrong there. - rfcc209
                # Set C[j] to S[c xor L]
                # should be
                # Set C[j] to (C[j] xor S[c xor L])
                checksum_bytes[i] = checksum_bytes[i] ^ Md2_u.pi_subst[ord(char) ^ previous]
                previous = checksum_bytes[i]

        checksum_string = str().join(chr(i) for i in checksum_bytes)
        return checksum_string

#todo : more merging with merkledamgaard and md4
class Md2(Merkledamgaard):
    """
    MD2 is based on the L{Merkle-Damgaard<Merkledamgaard>} model.

    padding is done according to pkcs7 standard, then an full block checksum is padded.
    """

    def __init__(self):
        Merkledamgaard.__init__(self)
        self.block_length = 16
        self.hv_size = 8
        self.IVs = bytes([0 for i in xrange(16)])

    def pad(self, message):
        padpkcs7 = Md2_u.padpkcs7(len(message))
        checksum = Md2_u.checksum(message + padpkcs7)
        return padpkcs7 + checksum

    def compute(self, message):
        self.ihvs = list(self.IVs)
        message += self.pad(message)
        block_bytes = [0 for i in xrange(16)]
        blocks = as_bytes_blocks(message, 16)

        for block in blocks:
            xor = bytes([0 for i in xrange(16)])
            block_bytes = [ord(i) for i in block]
            for i in xrange(16):
                xor[i] = self.ihvs[i] ^ block_bytes[i]

            previous = Byte(0)
            for round_ in xrange(18):
                for l in [self.ihvs, block_bytes, xor]:
                    for k in xrange(16):
                        previous = l[k] = l[k] ^ Md2_u.pi_subst[previous]
                previous = previous + round_
        return self


if __name__ == "__main__":
    import kbp.test.md2_test
