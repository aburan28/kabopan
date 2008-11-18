#Move to front
#entropy encoding
#A Locally Adaptive Data Compression Scheme
#J. L. Bentley, D. D. Sleator, R. E. Tarjan, V. K. Wei, 1986
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#Ange Albertini

def move_to_front(list, offset):
    """move to the front of the list the offset-th element"""
    return [list[offset]] + list[:offset] + list[offset + 1:]

assert move_to_front([0, 1, 2, 3, 4], 2) == [2, 0, 1, 3, 4]
assert move_to_front([0, 1, 2, 3, 4], 3) == [3, 0, 1, 2, 4]


def transform(data_to_compress):
    """apply a move to front transformation

    returns the transformation vector"""
    length = len(data_to_compress)

    chars = sorted(list(set(data_to_compress)))

    result = [0 for i in range(length)]
    for i in range(length):
        index = chars.index(data_to_compress[i])
        result[i] = index
        chars = move_to_front(chars, index)

    return result

assert transform("caraab") == [2, 1, 3, 1, 0, 3]


def revert(chars, vector):
    """apply a move to front reverse transformation to a list of chars
    and a transformation vector

    returns the transformed list"""
    length = len(vector)
    # assert chars == sorted(chars)

    result = ""
    for i in range(length):
        index = vector[i]
        result += chars[index]
        chars = move_to_front(chars, index)

    return result

assert revert(["a", "b", "c", "r"],[2, 1, 3, 1, 0, 3]) == "caraab"
