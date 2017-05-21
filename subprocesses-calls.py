#!/usr/bin/env python3 

import subprocess 

# Command 1 
uname = "uname"
uname_arg = "-a" 
print("Gathering System Information with {} command:\n".format(uname)) 
subprocess.call([uname, uname_arg]) 


# Command 2 

diskspace = "df" 
diskspace_arg = "-h"
print("Gathering Disk Information with {} command:\n".format(diskspace)) 
subprocess.call([diskspace, diskspace_arg]) 


