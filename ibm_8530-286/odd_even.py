#!/usr/bin/python
# ----------------------------------------------------------------------------
# converts .sid to .exo (crunched exomizer)
# ----------------------------------------------------------------------------
'''
Little tool to display SID info
'''
import sys
import os
import struct
import subprocess


__docformat__ = 'restructuredtext'


def run(odd_filename, even_filename):
    even_buf = None
    odd_buf = None

    with open(even_filename, "rb") as fd:
        even_buf = fd.read()

    with open(odd_filename, "rb") as fd:
        odd_buf = fd.read()

    print(type(even_buf))
    print(dir(even_buf))

    with open('output.bin', "wb") as fd:
        for i in range(len(even_buf)):
            b = even_buf[i:i+1]
            fd.write(b)
            b = odd_buf[i:i+1]
            fd.write(b)


def help():
    print("%s v0.1 - Utility tha converts .sid to .exo (crunched exomizer) files\n" % os.path.basename(sys.argv[0]))
    print("Example:\n%s *.sid" % os.path.basename(sys.argv[0]))
    sys.exit(-1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        help()

    run(sys.argv[1], sys.argv[2])
