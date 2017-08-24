#!/usr/bin/env python

import os
import sys
import string
import random
import math

letters = string.ascii_uppercase


def otp_gen(numbers):
    print "# Increment each character"
    print "# by the value in the pad."
    print "# Wrap Z->A for overflow."
    print "# Example: W + 6 = C"
    just = int(math.log(numbers)/math.log(10))+1
    pad = []

    # generate the pad
    for i in range(numbers):
        n = ord(os.urandom(1)) % len(letters)
        c = letters[n]
        v = string.join([str(i).rjust(just), str(ord(c)-ord('A')).rjust(2)])
        pad.append(v)

    # write out the values in columns
    cols = 4
    rows = int(math.ceil(len(pad)/float(cols)))
    for r in range(rows):
        for c in range(cols):
            p = c*rows+r
            if p < len(pad):
                print pad[p],
            if c < cols:
                print ' ',
        print

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage:", sys.argv[1], "[chars required] > otp.txt"
        sys.exit(-1)

    otp_gen(int(sys.argv[1]))
