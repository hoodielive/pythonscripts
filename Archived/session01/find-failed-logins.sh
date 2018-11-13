#!/bin/bash 
# Follow 'auth|authpriv' trail in syslog | identify failed entries
# On Deb6x, '/var/log/auth.log'
# Feb  1 22:01:42 debian sshd[14098]: Failed password for root from 10.0.1.31 port 51296 ssh2
# write simple script to parse '/var/log/auth.log'

# Define MYUSER and include root as a backup 
if [ -n "$1" ]; then 
	MYUSER="$1" 
	# check if $MYUSER exists 
	# Initalize Match Var 
	MATCH="0"

	#Iterate through list of MYUSERs  
	for i in $(awk -F : '{ print $1 }' /etc/passwd); do 
		if [ "$i" = "$MYUSER" ]; then 
			MATCH="1" 
		fi
	done  
	# If there is a Match - Continue
	if [ "$MATCH" = "0" ]; then 
		echo "MYUSER: $MYUSER does not exist on this system - Exiting..."
		exit 200
	fi 
fi 

# Define source file and message 
LOG=/var/log/auth.log 
MESSAGE="Failed password for $MYUSER"

# Parse source file for records for root
# If grep finds no match (none-zero exit status 'failure')
# Store results of search in a var and dump

echo $MESSAGE 
RECORDS=$(grep -i "$MESSAGE" $LOG) || echo "No Records Found for: $MYUSER"

if [ -n "$RECORDS" ]; then 
	echo "$RECORDS"
fi 
