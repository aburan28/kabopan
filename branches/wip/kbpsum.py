from getopt import *
from sys import argv, exit

try:
    import psyco
    psyco.run()
except:
    pass

import crc
import crypt.has160
import crypt.md2, crypt.md4, crypt.md5
import crypt.sha0, crypt.sha1, crypt.sha224, crypt.sha256, crypt.sha384, crypt.sha512
import crypt.ripemd128, crypt.ripemd160, crypt.ripemd256, crypt.ripemd320

digesttest = lambda m, s:m.compute(s).hexdigest()

families = [
    "crc", "has", "md", "ripemd", "sha",
    #"adler", "flechter", "gost", "haval", "lm", "panama", "tiger", "whirlpool", "snefru",
    ]
algorithms = {
    "crc32_ieee":crc.crc32_ieee_hexhash,
    "has-160":lambda x:crypt.has160.has160().compute(x).hexdigest(),
    "md2":lambda x:crypt.md2.md2().compute(x).hexdigest(),
    "md4":lambda x:crypt.md4.md4().compute(x).hexdigest(),
    "md5":lambda x:crypt.md5.md5().compute(x).hexdigest(),
    "ripemd-128":lambda x:crypt.ripemd128.ripemd128().compute(x).hexdigest(),
    "ripemd-160":lambda x:crypt.ripemd160.ripemd160().compute(x).hexdigest(),
    "ripemd-256":lambda x:crypt.ripemd256.ripemd256().compute(x).hexdigest(),
    "ripemd-320":lambda x:crypt.ripemd320.ripemd320().compute(x).hexdigest(),
    "sha-0"     :lambda x:crypt.sha0.sha0().compute(x).hexdigest(),
    "sha-1"     :lambda x:crypt.sha1.sha1().compute(x).hexdigest(),
    "sha-224"   :lambda x:crypt.sha224.sha224().compute(x).hexdigest(),
    "sha-256"   :lambda x:crypt.sha256.sha256().compute(x).hexdigest(),
    "sha-384"   :lambda x:crypt.sha384.sha384().compute(x).hexdigest(),
    "sha-512"   :lambda x:crypt.sha512.sha512().compute(x).hexdigest(),
    #"adler32":_,
    #"flechter16":_,
    #"flechter32":_,
    #"gost":_,
    #"haval":_,
    #"panama":_,
    #"lm":_,
    #"snefru":_,
    #"tiger":_,
    #"tiger2":_,
    #"whirlpool":_,
    }
Help = "Kabopan checksum calculator\n"
Help +=  "Parameters:  [-a algorithm] <[-f <input file>]|[<text>]>\n"
Help += "Algorithms:\n\t"+ "\n\t".join([", ".join([a for a in sorted(algorithms) if a.startswith(f)]) for f in families])

if len(argv) == 1:
    print(Help)
    exit()

opts = "a:f:"
try:
    optlist, args = getopt(argv[1:], opts)
    optlist = dict(optlist)

    if "-a" not in optlist:
        requested_algorithms = sorted(algorithms.keys())
    else:
        if optlist["-a"] not in algorithms:
            raise GetoptError("algorithm not found")
        else:
            requested_algorithms = [optlist["-a"]]
    if len(args) == 0 and "-f" not in optlist:
        raise GetoptError("missing text or file")
    if "-f" in optlist:
        with open(optlist["-f"], "rb") as f:
            input = f.read()
    else:
        input = " ".join(args)

except GetoptError, error:
    print("Error: %s\n" % error)
    print(Help)
    exit()

if len(requested_algorithms) == 1:
    print "%s" % (algorithms[requested_algorithms[0]](input))
else:
    for s in requested_algorithms:
            print "%s\t%s" % (s, algorithms[s](input))
