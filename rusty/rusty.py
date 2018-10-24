#!/usr/bin/env python3 

import sys
import re
import getopt 

def usage(code, msg=''):
    if code:
        fd = sys.stderr
    else:
        fd = sys.stdout
    print >> fd, _(__doc__) 
    if msg:
        print >> fd, msg
    sys.exit(code)

