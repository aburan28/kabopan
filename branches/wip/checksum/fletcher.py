#Flechter checksum - Flechter-16/32
#Fletcher, J. G., An Arithmetic Checksum for Serial Transmissions
#1982
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

def calculate(data_to_checksum, size, modulo, limit=None):
    sum, sum_of_sum = 1, 0

    length = len(data_to_checksum)
    if limit is not None and length > limit:
        data_to_checksum = data_to_checksum[:limit]
    for char in data_to_checksum:
        sum += ord(char)
        sum_of_sum += sum
        sum %= modulo
        sum_of_sum %= modulo
    return (sum_of_sum << (size / 2)) + sum

def get_adler_limit():
    return max(n for n in xrange(2 ** (32 / 2)) if (255 * n * (n + 1)/2 + (n + 1) * (65521- 1) <= 2 ** 32 - 1))


def Fletcher16(data_to_checksum):
    return calculate(data_to_checksum, 256, limit=21)


def Fletcher32(data_to_checksum):
    return calculate(data_to_checksum, 65536, limit=360)


def Adler32(data_to_checksum):
    return calculate(data_to_checksum, 32, 65521, limit=5552)


if __name__ == "__main__":
    import fletcher_test
