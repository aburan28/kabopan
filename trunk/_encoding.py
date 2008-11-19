#Useful Functions for entropy encoding algorithms, such as Shannon Fano or Huffman
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#Ange Albertini

def generate_codes(node, codes=None, current_code=""):
    """walk the encoding tree and generates code for symbol (in leaves)"""
    if codes is None:
        codes = {}
    if "symbol" in node:
        codes[node["symbol"]] = current_code
        return codes
    else:
        generate_codes(node["left0"], codes, current_code + "0")
        generate_codes(node["right1"], codes, current_code + "1")
    return codes

assert generate_codes({'left0': {'symbol': 'a', 'weight': 1},
                     'right1': {'symbol': 'b', 'weight': 1},
                     'weight': 2}) == {'a': '0', 'b': '1'}

def get_weights_and_symbols(data):
    stats = [{"symbol": chr(i), "weight": 0} for i in range(256)]
    for char in data:
        stats[ord(char)]["weight"] += 1
    stats = [i for i in stats if i["weight"] > 0]
    return stats

assert get_weights_and_symbols("a") == [{"symbol":"a","weight":1}]
assert get_weights_and_symbols("abababbc") == [{"symbol":"a","weight":3},
                                               {"symbol":"b","weight":4},
                                               {"symbol":"c","weight":1},]

def encode_string(codes, string):
    import _bits
    comp = _bits.compress(1)
    for char in string:
        comp.write_bitstring(codes[char])
    result = comp.getdata()
    return result

def decode_string(tree_root, string):
    result = ""
    import _bits
    decomp = _bits.decompress(string, 1)
    while not decomp.is_end():
        node = tree_root
        while "symbol" not in node:
            bit = decomp.read_bit()
            if bit == 0:
                node = node["left0"]
            elif bit == 1:
                node = node["right1"]
        result += node["symbol"]
    return result