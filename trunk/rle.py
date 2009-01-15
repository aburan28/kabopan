#Run-length encoding
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


def compress(data_to_compress):
    offset = 0
    repetition = 0
    compressed_data = []
    length = len(data_to_compress)

    while offset < length:
        char = data_to_compress[offset]
        repetition = 0
        while offset + repetition < length and data_to_compress[offset + repetition] == char:
            repetition += 1

        compressed_data.append([repetition, char])
        offset += repetition
    return compressed_data


def decompress(compressed_data):
    decompressed_string = ""
    for repetition, char in compressed_data:
        decompressed_string += char * repetition
    return decompressed_string


test = "abababababaaaaaaccccccccbcdbcksjcblsauiaaaauu"



assert compress(test) == [[1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'], [1, 'a'], [1, 'b'],
                    [1, 'a'], [1, 'b'], [6, 'a'], [8, 'c'], [1, 'b'], [1, 'c'], [1, 'd'], [1, 'b'],
                    [1, 'c'], [1, 'k'], [1, 's'], [1, 'j'], [1, 'c'], [1, 'b'], [1, 'l'], [1, 's'],
                    [1, 'a'], [1, 'u'], [1, 'i'], [4, 'a'], [2, 'u']]
assert decompress(compress(test)) == test
