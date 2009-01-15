#Useful Functions for sliding window compression algorithms, such as LZ77
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python



#TODO: proper longest match implementation

def find_longest_match(s, sub):
    """returns the number of byte to look backward and the length of byte to copy)"""
    if sub == "":
        return 0, 0
    limit = len(s)
    dic = s[:]
    l = 0
    offset = 0
    length = 0
    first = 0
    word = ""

    word += sub[l]
    pos = dic.rfind(word, 0, limit + 1)
    if pos == -1:
        return offset, length

    offset = limit - pos
    length = len(word)
    dic += sub[l]

    while l < len(sub) - 1:
        l += 1
        word += sub[l]

        pos = dic.rfind(word, 0, limit + 1)
        if pos == -1:
            return offset, length
        offset = limit - pos
        length = len(word)
        dic += sub[l]
    return offset, length

assert find_longest_match("abc","a") == (3,1)
assert find_longest_match("abc","d") == (0,0)
assert find_longest_match("abcab","ab") == (2,2)

def back_copy(string, length, offset):
    for i in xrange(length):
        string += string[-offset]
    return string
    
assert back_copy("a",1,1) == "aa"
assert back_copy("ab",2,2) == "abab"
assert back_copy("duplicate me please",9,19) == "duplicate me pleaseduplicate"

