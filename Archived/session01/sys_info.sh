#!/bin/bash 

uname_func()
{
	UNAME=$(uname -a) 
	printf "Gathering system information with $UNAME command:\n\n" 
	$UNAME 

} 

disk_func() 
{
	DISKSPACE=$(df -h) 
	printf "Gather disk space information with $DISKSPACE command:\n\n" 
	$DISKSPACE

} 

function main() 
{
	uname_func() 
	disk_func() 

} 

main
