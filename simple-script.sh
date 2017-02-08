#!/bin/bash

TOTAL=0

for filename in *; do 
	if [ -f $filename ] ; then 
		./$filename
		TOTAL=$((TOTAL+1))
	fi
done

echo $TOTAL scripts started
