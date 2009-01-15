#Lempel Ziv 78 - LZ78 - LZ2
#lossless dictionary (dynamic dictionary) coder (compression algorithm)
#Compression of Individual Sequences via Variable-Rate Coding
#Jacob Ziv and Abraham Lempel, 1978
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


def compress(data_to_compress):
    offset = 0
    compressed_data = []
    dictionary = []

    length = len(data_to_compress)

    while offset < length:
        word = ''
        word_size = len(word)
        char = data_to_compress[offset + word_size]

        #add the next char as long as the current word is found in the dictionary
        while (word + char) in dictionary and (offset + word_size) < length:
            word = word + char
            word_size = len(word)
            char = data_to_compress[offset + word_size]

        if len(word) > 0:
            index_ = dictionary.index(word)
            index_ += 1      #if 0 then not present in the dictionary
        else:
            index_ = 0
        compressed_data.append({"index":index_, "symbol":char})

        offset += len(word + char)
        dictionary.append(word + char)

    return compressed_data

assert compress("abracadabra") == [{'index': 0, 'symbol': 'a'}, {'index': 0, 'symbol': 'b'}, {'index': 0, 'symbol': 'r'},
                             {'index': 1, 'symbol': 'c'}, {'index': 1, 'symbol': 'd'},
                             {'index': 1, 'symbol': 'b'}, {'index': 3, 'symbol': 'a'}]


def decompress(compressed_data):
    decompressed_string = ""
    dictionary = []
    for d in compressed_data:
        char, index_ = d["symbol"], d["index"]

        #if the index is not null, get the corresponding word from the dictionary,
        #otherwise the word is empty
        if index_ > 0:
            index_ -= 1         # dictionary index is 0-based
            word = dictionary[index_]
        else:
            word = ""

        decompressed_string += word + char
        dictionary.append(word + char)

    return decompressed_string

assert decompress(compress("abracadabra")) == "abracadabra"
