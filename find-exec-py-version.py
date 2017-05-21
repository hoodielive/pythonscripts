#!/usr/bin/env python3 

import os, subprocess

for dirpath, dirname, filename in os.walk('.'):
    subprocess.check_call(['stat', dirpath]) 
    for file in filename: 
        filepath = os.path.join(dirpath, filename)
        subprocess.check_call(['stat', filepath]) 



