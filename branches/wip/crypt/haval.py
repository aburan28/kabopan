"""Haval
cryptographic hash
HAVAL --- a one-way hashing algorithm with variable length of output
Yuliang Zheng, Josef Pieprzyk, Jennifer Seberry 1992
http://labs.calyptix.com/haval.php
"""
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004
"""
collision, as dwords...
6377448b d9e59f18 f2aa3cbb d6cb92ba ee544a44 879fa576 1ca34633 76ca5d4f
a67a8a42 8d3adc8b b6e3d814 5630998d 86ea5dcd a739ae7b 54fd8e32 acbb2b36
38183c9a b67a9289 c47299b2 27039ee5 dd555e14 839018d8 aabbd9c9 d78fc632
fff4b3a7 40000096 7f466aac fffffbc0 5f4016d2 5f4016d0   12e2b0 f4307f87

6377488b d9e59f18 f2aa3cbb d6cb92ba ee544a44 879fa576 1ca34633 76ca5d4f
a67a8a42 8d3adc8b b6e3d814 d630998d 86ea5dcd a739ae7b 54fd8e32 acbb2b36
38183c9a b67a9289 c47299ba 27039ee5 dd555e14 839018d8 aabbd9c9 d78fc632
fff4b3a7 40000096 7f466aac fffffbc0 5f4016d2 5f4016d0   12e2b0 f4307f87"""

#from mpmath import *
#mp.dps = 50
#from fractions import *
#from decimal import Decimal, getcontext
#getcontext().prec=2000
#p = Decimal(0)
#for i in range(200):
#	p += Decimal(4*(-1)**i) / Decimal(2*i+1)
#print p
#4*(-1)**n/(2*n+1)
from sympy import *
#_1310_digits_of_float_part_of_pi_in_hex = 
print "%x" % int((pi.evalf(n=2000) - 3)* 2 ** (32 * 136))