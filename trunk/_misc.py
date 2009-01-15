#various functions for binary calculations, display...
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


#todo : a lot of cleaning is likely required

def gcd(a,b):    
    return gcd(b, a % b) if b != 0 else a

def lcm(a,b):
    return a * b / gcd(a,b)


def getbinlen(value):
    """return the bit length of an integer"""
    result = 0
    if value == 0:
        return 1
    while value != 0:
        value >>= 1
        result += 1
    return result

assert getbinlen(0) == 1
assert getbinlen(1) == 1
assert getbinlen(3) == 2


def getlongestcommon(a, b):
    """returns i, maximum value such that a[:i] == b[:i]"""
    l = min(len(i) for i in  [a, b])
    res = 0
    while res < l and a[res] == b[res]:
        res += 1
    return res

assert getlongestcommon("31415926535", "31416")  == 4


def gethyphenstr(s, limit = 9, sep = " [...] "):
    """turns a long string into a [...]-shortened string"""
    if len(s) > 2*limit + len(sep):
        return s[:limit].rstrip() + sep + s[-limit:].lstrip()
    else:
        return s

assert gethyphenstr(r"c:\WINDOWS\system32\drivers\http.sys") == r"c:\WINDOW [...] \http.sys"


def getbinstr(value):
    """return the smallest binary representation of an integer"""
    if value == 0:
        return "0"

    result = ""
    while value != 0:
        if value & 1:
            result = "1" + result
        else:
            result = "0" + result
        value >>= 1
    return result

assert getbinstr(0) == "0"
assert getbinstr(8) == "1000"

def getvaluefrombinarystring(string):
    result = 0
    for char in string:
        bit = 1 if char == "1" else 0
        result = (result << 1) + bit
    return result

assert getvaluefrombinarystring("1000") == 8
assert getvaluefrombinarystring("001000") == 8
    
def countmissing(value, modulo):
    """returns x > 0 so that (value + x) % modulo = 0 (useful to write leading zeroes)"""
    result = value % modulo
    if result == 0:
        result = modulo
    return modulo - result

assert countmissing(0,8) == 0
assert countmissing(3,8) == 5
assert countmissing(8,8) == 0


def getpadbinstr(value,bits):
    """return a 0-padded binary string."""
    s = getbinstr(value)
    l = len(s)
    mod = countmissing(l,bits)
    return "0" * mod + s

assert getpadbinstr(8, 8) == "00001000"


def getunkbinstr(value, currentbit, maxbit):
    """returns a binary string representation of the command/tag

    including unset bits, according to currentbit.
    it displays 'value' as a binary string, padded according to 'maxbit',
    then hides the lowest bits until 'currentbit'"

    """
    s = getpadbinstr(value, maxbit + 1)[:maxbit - currentbit + 1]
    mod = countmissing(len(s), maxbit + 1)
    return s + "x" * mod

assert getunkbinstr(0,0,8) == "000000000"
assert getunkbinstr(1,0,8) == "000000001"
assert getunkbinstr(2,1,8) == "00000001x"
assert getunkbinstr(237,3,8) == "011101xxx"


def gethexstr(string):
    return " ".join("%02X" % (ord(char)) for char in string)

assert gethexstr("\x00") == "00"
assert gethexstr("\x00\x01") == "00 01"
assert gethexstr("abcd") == "61 62 63 64"


def int2lebin(value, size):
    """ouputs value in binary, as little-endian"""
    result = ""
    for i in xrange(size):
        result = result + chr((value >> (8 * i)) & 0xFF )
    return result

assert int2lebin(1,2) == '\x01\x00'
assert int2lebin(65535,2) == "\xff\xff"
assert int2lebin(65535,3) == "\xff\xff\x00"

def int2bebin(value, size):
    """ouputs value in binary, as big-endian"""
    result = ""
    for i in xrange(size):
        result = chr((value >> (8 * i)) & 0xFF ) + result
    return result

assert int2bebin(1,2) == '\x00\x01'

def md5(s):
    """returns hex digest of the md5 of the string"""
    import hashlib
    return hashlib.md5(s).hexdigest()

assert md5("") == "d41d8cd98f00b204e9800998ecf8427e"


def modifystring(s, sub, offset):
    """overwrites 'sub' at 'offset' of 's'"""
    return s[:offset] + sub + s[offset + len(sub):]

assert modifystring("abcd","_",2) == "ab_d"
assert modifystring("abcde","=+",2) == "ab=+e"

#todo : sort what's next
def brutting_snippet(data, function):
    maxlen = 0
    result = {}
    for i in xrange(50):
        blz = function(data[i:])
        decomp, consumed = blz.do()
        maxlen = max(len(decomp), maxlen)
        result[len(decomp)] = i
        print

    print result
    print maxlen, result[maxlen]
    return result[maxlen]

def write_snippet(filename, data):
    f = open(filename + ".out", "wb")
    for i in data:
        f.write(i)
    f.close()

def checkfindest(dic, stream, offset, length):
    """checks that findlongeststring result is correct"""
    temp = dic[:]
    for i in xrange(length):
            temp += temp[-offset]
    if temp != dic + stream[:length]:
        print temp
        print dic + stream[:length]
        return False
    return True

