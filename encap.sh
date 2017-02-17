#!/bin/bash

eval "`date "+DATE=%Y-%m-%d"`"
src=$HOME/Documents/uploads/scripts
dest=redadmin@10.0.1.77:~
[ -f "$src" ] && scp -p "$src" "$dest"
