#Huffman coding - Huffman tree
#entropy encoding
#A Method for the Construction of Minimum-Redundancy Codes
#D.A. Huffman 1952
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#Ange Albertini

import _encoding

def pop_entry(stats):
    """clears the first entry in the list
    return the symbol and weight, or the node itself."""
    entry = stats.pop(0)
    if "node" not in entry:
        node = entry
    else:
        node = entry["node"]
    return node

assert pop_entry([{"symbol":"a", "weight" : 15}]) == {"symbol":"a", "weight":15}
assert pop_entry([{"node":"this"}]) == "this"

def generate_huffman_tree(data_to_compress):

    # stats first contains symbols and their weights,
    # then parent nodes and their weights as well, while the tree is built
    stats = _encoding.get_weights_and_symbols(data_to_compress)
    stats = sorted(stats, key = lambda x:x["weight"])

    # as long as we have more than one element to process, we'll grow the tree
    while len(stats) > 1:
        # let's create a parent node
        parent_node = {"left0": None, "right1": None, "weight": 0}

        # the 2 children are the first and second elements of the list
        parent_node["left0"]= pop_entry(stats)
        parent_node["right1"]= pop_entry(stats)

        # and the weight is the sum of both children's
        cumulative_weight = parent_node["left0"]["weight"] + parent_node["right1"]["weight"]

        parent_node["weight"] = cumulative_weight

        # let's add a new entry in the list for the recently created parent node
        entry = {"node": None, "weight": 0}
        entry["node"] = parent_node
        entry["weight"] = cumulative_weight

        stats.append(entry)

        # and re-sort the list
        stats = sorted(stats, key = lambda x:x["weight"])

    # we just have one entry left - the root of the tree - let's return it.
    root_node = pop_entry(stats)
    return root_node


tree_test = generate_huffman_tree("a")
assert tree_test == {'symbol': 'a', 'weight': 1}
assert _encoding.generate_codes(tree_test) == {"a":""}

test_string = "abracadabra"
test_tree = generate_huffman_tree(test_string)
assert test_tree == {'left0': {'symbol': 'a', 'weight': 5},
                     'right1': {'left0': {'left0': {'symbol': 'c', 'weight': 1},
                                          'right1': {'symbol': 'd', 'weight': 1},
                                          'weight': 2},
                                'right1': {'left0': {'symbol': 'b', 'weight': 2},
                                           'right1': {'symbol': 'r', 'weight': 2},
                                           'weight': 4},
                                'weight': 6},
                     'weight': 11}

test_codes = _encoding.generate_codes(test_tree)
assert test_codes == {'a':'0', 'c':'100', 'd':'101', 'b':'110', 'r':'111'}

encoded_string = _encoding.encode_string(test_codes, "abracadabra")
assert encoded_string == 'n\x8a\xdc'
assert _encoding.decode_string(test_tree, encoded_string) == test_string