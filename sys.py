#!/usr/bin/python3 

import sys, os 

#sys.path 

# the ! is a functionality that can only be invoked in jupyter or ipython 

for path in sys.path:
	print("-----------------------")
	if os.path.isdir(path):
	  !echo $path; cd $path; find . -name \*.py -or -name \*.so
	else:
		print(path)
