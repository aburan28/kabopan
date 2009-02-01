#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from lz78 import *

assert compress("abracadabra") == [
    {'index': 0, 'symbol': 'a'}, {'index': 0, 'symbol': 'b'}, {'index': 0, 'symbol': 'r'},
    {'index': 1, 'symbol': 'c'}, {'index': 1, 'symbol': 'd'},
    {'index': 1, 'symbol': 'b'}, {'index': 3, 'symbol': 'a'}]

assert decompress(compress("abracadabra")) == "abracadabra"

