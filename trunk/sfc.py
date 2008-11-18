#Shannon-Fano coding
#Entropy encoding
#A Mathematical Theory of Communication
#Claude E. Shannon, 1948
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#Ange Albertini

import _encoding

def split(list, index):
    """split the list in 2 halves AFTER the index parameter"""
    return list[:index + 1], list[index + 1:]

assert split([0,1,2,3],1) == ([0,1], [2,3])
assert split([0,1,2,3],0) == ([0], [1,2,3])

def split_weights(weights):
    """returns the index of a list of weight, after which the list is split in 'almost equal' halves
    ie when the difference of cumulated weights of both parts is minimal"""
    length = len(weights)

    increasing_weights = [sum(weights[:i + 1]) for i in range(length)]
    decreasing_weights = [sum(weights[i:]) for i in range(length)]
    differences = [abs(increasing_weights[i] - decreasing_weights[i + 1])
                   for i in range(length - 1)]

    half_weight = min(differences)
    half_index = differences.index(min(differences))
    return half_index

assert split_weights([1,1]) == 0
assert split_weights([1,2,3]) == 1
assert split_weights([8,7,1]) == 0
assert split_weights([1,1,8]) == 1


def generate_sfc_tree(elements):
    """generate a shannon fano tree out of a list of dictionaries of symbols and their weights"""
    if len(elements) == 1:
        node = {"symbol":elements[0]["symbol"]} # nothing to split - it's a leaf
    else:
        weights = [e["weight"] for e in elements]
        half_weight_index = split_weights(weights)

        left_half, right_half = split(elements, half_weight_index)

        left_node = generate_sfc_tree(left_half)
        right_node = generate_sfc_tree(right_half)

        node = {"left0": left_node, "right1": right_node}

    return node


assert generate_sfc_tree([{"symbol":"a", "weight":35}]) == {"symbol":"a"}
assert generate_sfc_tree([{"symbol":"a", "weight":2},
                          {"symbol":"b", "weight":2}]) == {'left0': {'symbol': 'a'},
                                                           'right1': {'symbol': 'b'}}

def encode(data_to_compress):
    stats = _encoding.get_weights_and_symbols(data_to_compress)    

    stats = sorted(stats, key = lambda x:x["weight"], reverse = True)

    tree = generate_sfc_tree(stats)

    return tree


tree_test = encode("abracadabra")
assert tree_test == {'left0': {'symbol': 'a'},
                     'right1': {'left0': {'symbol': 'b'},
                                'right1': {'left0': {'symbol': 'r'},
                                           'right1': {'left0': {'symbol': 'c'},
                                                      'right1': {'symbol': 'd'}}}}}

assert _encoding.generate_codes(tree_test) == [['a', '0'], ['b', '10'], ['r', '110'],
                                               ['c', '1110'], ['d', '1111']]
