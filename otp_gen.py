#!/usr/bin/env python

import os
import sys
import string
import random
import math

letters = string.ascii_uppercase

def otp_gen(numbers):
	print "# Increment the character at the index"
	print "# by the value of the letter below."
	print "# Wrap Z->A for overflow."
	just = int(math.log(numbers)/math.log(10))+1
	for i in range(numbers):
		n = ord(os.urandom(1))%len(letters)
		c = letters[n]
		print str(i).rjust(just), c, str(ord(c)-ord('A')).rjust(2)

if __name__ == "__main__":
	if len(sys.argv)<=1:
		print "Usage:",sys.argv[1],"[chars required] > otp.txt"
		sys.exit(-1)

	otp_gen(int(sys.argv[1]))
