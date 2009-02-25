#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.coder.playfair import encode, decode

assert encode("Hide the gold in the tree stump", "PLAYFAIR EXAMPLE") == "BMNDZBXDKYBEJVDMUIXMMNUVIF"

assert decode("BMNDZBXDKYBEJVDMUIXMMNUVIF", "PLAYFAIR EXAMPLE") == "HIDETHEGOLDINTHETREXESTUMP" # note the extra X, which is normal.