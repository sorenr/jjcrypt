#!/usr/bin/env python

import sys
import otp_gen

# retrieve the value from the one-time-pad


def otp_get(otp_fd, index):
    while True:
        try:
            return otp_get.pad[index]
        except KeyError:
            # read a line from the pad
            line = otp_fd.readline()
            if not line:
                print "pad too short."
                sys.exit(-1)
            # skip comment lines
            if line.startswith('#'):
                continue
            line = line.split()
            # add the values into the pad
            while line:
                otp_get.pad[int(line[0])] = int(line[1])
                line = line[3:]
otp_get.pad = {}


def otp_crypt(direction, otp_fd, message):
    message = message.upper()
    cryptext = ""
    for i in range(len(message)):
        if message[i] not in otp_gen.letters:
            cryptext = cryptext + message[i]
            continue
        n = otp_get(otp_fd, i)
        cc = (ord(message[i])-ord('A')+(n*direction)) % 26
        cryptext = cryptext + chr(cc+ord('A'))
    print cryptext

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage:", sys.argv[0], "[ -c | -d ] otp.txt message"

    if sys.argv[1][1] == 'c':
        val = -1
    elif sys.argv[1][1] == 'd':
        val = 1
    else:
        print "Pleas select encrypt (-c) or decrypt (-d)."
        sys.exit(-1)

    otp_crypt(val, open(sys.argv[2]), sys.argv[3])
