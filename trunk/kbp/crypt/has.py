#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Hash function Algorithm Standard, HAS-160

cryptographic hash
TTAS.KO-12.0011/R1
Telecommunications Technology Association
"""

from kbp._misc import hsqrt
from kbp.types import Qword, Utility
from kbp.crypt.sha import Sha0, Sha_u
from kbp.crypt.md4 import Md4_u, Md5_u


class Has160_u(Utility):
    """utility class for has-160 cryptographic hash"""

    constants = [hsqrt(i) for i in [0, 2, 3, 5]]
    extensions = [
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
        [[3, 6, 9, 12], [15, 2, 5, 8], [11, 14, 1, 4], [7, 10, 13, 0]],
        [[12, 5, 14, 7], [0, 9, 2, 11], [4, 13, 6, 15], [8, 1, 10, 3]],
        [[7, 2, 13, 8], [3, 14, 9, 4], [15, 10, 5, 0], [11, 6, 1, 12]]]

    # indexes are like extensions (flattened), with 18, 19, 16, 17 inserted every 4 value
    indexes = list()
    for extension in extensions:
        #pylint: disable-msg=E0602
        insert_every_four = ([[18, 19, 16, 17][i]] + j for i, j in enumerate(extension))
        indexes += [ sum(insert_every_four, [])]

class Has160(Sha0):
    """
    has-160 is based on sha-0.

    changes:
     - output, input, and size encoding are little endian
     - a and b rotation parameter are different at each iteration
     - only 20 words, which are recomputed differently, for each round.
     - the round-specific functions are md4.f, md4.h, md5.i, md4.h respectively
    """
    def __init__(self):
        Sha0.__init__(self)
        self.output_big_endianness = self.block_big_endianness = self.padding_big_endianness = False

    def rounds(self, words):
        words.extend((0 for i in xrange(20-16)))
        a, b, c, d, e = list(self.ihvs)
        for r in range(4):
            f = [Md4_u.f, Md4_u.h, Md5_u.i, Md4_u.h][r]
            k = Has160_u.constants[r]
            b_rot = [10, 17, 25, 30][r]

            for i in range(4):
                w = Qword(0)
                for j in xrange(4):
                    w ^= words[Has160_u.extensions[r][i][j]]
                words[16 + i] = w

            for i in range(20):
                index = Has160_u.indexes[r][i]
                a_rot = [5, 11, 7, 15, 6, 13, 8, 14, 7, 12, 9, 11, 8, 15, 6, 12, 9, 14, 5, 13][i]

                a, b, c, d, e = Sha_u.round_f(a, b, c, d, e, f, a_rot, b_rot, words, index, k)
        return [a, b, c, d, e]

if __name__ == "__main__":
    import kbp.test.has_test