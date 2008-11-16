#Lempel Ziv Welch - LZW
#lossless dictionary (dynamic) coder (compression algorithm)
#A Technique for High-Performance Data Compression
#Terry A. Welch, 1984
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python
#Ange Albertini

def compress(data_to_compress):
    """compress using LZW.
    return roots (present symbols in the data to compress)
    and the LZW-compressed data (indexes representing either an entry in the dictionary, or the need to create a new entry)"""
    offset = 0
    compressed_data = []
    roots = list(set(data_to_compress))
    dictionary = roots[:]

    length = len(data_to_compress)
    word = ''
    while offset < length:

        char = data_to_compress[offset]

        if (word + char) in dictionary:
            word = word + char
        else:
            compressed_data.append(dictionary.index(word))
            dictionary.append(word + char)
            word = char
        offset += 1
    compressed_data.append(dictionary.index(word))

    return roots, compressed_data

assert compress("abracadabra") == (['a', 'r', 'b', 'c', 'd'],
                                   [0, 2, 1, 0, 3, 0, 4, 5, 7])


def decompress(roots, compressed_data):
    decompressed_data = ""
    dictionary = roots

    #the first index has to be one of the root. decompressed_data is started.
    current_index = compressed_data[0]
    decompressed_data += dictionary[current_index]

    #now we'll read all the remaining indexes, and remember the previous one
    for index_ in compressed_data[1:]:
        previous_index = current_index
        current_index = index_
        word = dictionary[previous_index]

        if current_index < len(dictionary): # if the index is within the dictionary size,
            char = dictionary[current_index][0]

            decompressed_data += dictionary[current_index]
        else:
            char = dictionary[previous_index][0]

            decompressed_data += word + char

        dictionary.append(word + char)

    return decompressed_data

assert decompress(*compress("abracadabra")) == "abracadabra"
