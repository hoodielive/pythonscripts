#!/bin/bash

function check_usage()
{
	echo "Usage: $0 is the name of the script"
	exit 1

}

# Main program will commence:
		
	if [ $# -ne 2 ] ; then 
	
		check_usage
	else
		echo "Starting.. my series" 

	fi

	#else 
		if [ -d $1 ] ; then 
			source_dir=$1

		else
			echo "Invalid source directory" 
			check_usage

		fi 


		if [ -d $2 ] ; then
			dest_dir=$2 

		else 
			echo "Invalid destination directory"
			check_usage

		fi
	

	printf "Source directory is ${source_dir}\n" 
	printf "Destination directory is ${dest_dir}\n" 
	
