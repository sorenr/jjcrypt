#!/usr/bin/env python

import sys
import otp_gen

def otp_crypt(direction,otp_fd,message):
	message = message.upper()
	print "V>",otp_gen.letters
	cryptext = ""
	for i in range(len(message)):
		if message[i] not in otp_gen.letters:
			cryptext = cryptext + message[i]
			continue
		while True:
			line = otp_fd.readline()
			if line and line[0] != '#':
				break
		n = int(line.split()[2])
		cc = ( ord(message[i])-ord('A')+(n*direction) ) % 26
		cryptext = cryptext + chr(cc+ord('A'))
	print ["CT>",cryptext]

if __name__=="__main__":
	if len(sys.argv)<=1:
		print "Usage:",sys.argv[0],"[ -c | -d ] otp.txt message"

	if sys.argv[1][1]=='c':
		val = -1
	elif sys.argv[1][1]=='d':
		val = 1
	else:
		print "Pleas select encrypt (-c) or decrypt (-d)."
		sys.exit(-1)

	otp_crypt(val,open(sys.argv[2]),sys.argv[3])
