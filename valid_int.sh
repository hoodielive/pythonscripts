#!/bin/bash 
validint()
{
	# Validate first field and test that value against min value $2 and or max value $3 if they are supplied
	# If the value is not within range or its not composed of just digits, fail. 

	number=$1; 	min=$2; max=$3; 

	if [ -z $number ] ; then 

		echo "You didn't enter anything. Please remember." >&2 
		return 1
	fi 

	# Is the first character a '-' sign? 
	if [ "${number%${number#?}}" = '-'] ; then
		testvalue="${number#?}" # Grab all but the first character to test. 
	else
		testvalue=$number 
	fi 
}