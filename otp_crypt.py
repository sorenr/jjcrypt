#!/usr/bin/env python

import sys
import argparse
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
            line = map(int,line.split())
            # add the values into the pad
            while line:
                otp_get.pad[line[0]] = line[1]
                line = line[2:]
otp_get.pad = {}


def otp_crypt(direction, otp_fd, message, args):
    message = message.upper()
    cryptext = ""
    for i in range(len(message)):
        if message[i] not in otp_gen.letters:
            cryptext = cryptext + message[i]
            continue
        n = otp_get(otp_fd, i)
        cc = (ord(message[i])-ord('A')+(n*direction)) % 26
        cc = chr(cc+ord('A'))
        cryptext = cryptext + cc
        if args.v:
            print[i, message[i], n, cc]
    print cryptext

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Encrypt/decrypt with a one time pad.')
    parser.add_argument('-d', action='store_true', help='decrypt')
    parser.add_argument('-e', action='store_true', help='encrypt')
    parser.add_argument('-v', action='store_true', help='verbose')
    parser.add_argument('others', nargs='*')
    args = parser.parse_args()

    if len(args.others) <= 1:
        print "Usage:", sys.argv[0], "[ -c | -d ] otp.txt message"

    if args.e:
        val = -1
    elif args.d:
        val = 1
    else:
        print "Pleas select encrypt (-c) or decrypt (-d)."
        sys.exit(-1)

    otp_crypt(val, open(args.others[0]), args.others[1], args)
