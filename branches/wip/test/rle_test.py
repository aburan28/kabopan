#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from rle import *

test = "abababababaaaaaaccccccccbcdbcksjcblsauiaaaauu"

assert compress(test) == [[1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'],
                    [1, 'a'], [1, 'b'], [6, 'a'], [8, 'c'], [1, 'b'], [1, 'c'], [1, 'd'], [1, 'b'],
                    [1, 'c'], [1, 'k'], [1, 's'], [1, 'j'], [1, 'c'], [1, 'b'], [1, 'l'], [1, 's'],
                    [1, 'a'], [1, 'u'], [1, 'i'], [4, 'a'], [2, 'u']]
assert decompress(compress(test)) == test
