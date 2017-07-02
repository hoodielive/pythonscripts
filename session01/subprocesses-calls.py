#!/usr/bin/env python3 

import subprocess 

def uname_func(): 
# Command 1 
uname = "uname"
uname_arg = "-a" 
print("Gathering System Information with {} command:\n".format(uname)) 
subprocess.call([uname, uname_arg]) 



def diskspace_func(): 
# Command 2 

diskspace = "df" 
diskspace_arg = "-h"
print("Gathering Disk Information with {} command:\n".format(diskspace)) 
subprocess.call([diskspace, diskspace_arg]) 


def main():
    uname_func()
    diskspace_func() 

main() 
