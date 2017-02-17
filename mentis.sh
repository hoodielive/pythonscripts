#!/bin/bash

menu1()
{
	m1_items=$# ## number of commands (i.e., arguments)
	while:  	## Endless loops
	do
		printf "%s " "$menu"
		get_key Q 	
		case $Q in 
			O|q|"$NL")
				printf "\n"; break ;; ## break out
			[1-$m1_items])
				printf "\n"
				( eval "\$$Q" )
				case $pause_after in 
					*?) press_any_key 
						;; 
				esac 
				;; 
			*) printf "\n\t\a%Invalid entry: %s\n" "${progname:+$progname: }" "$Q"
				continue 
				;; 
		esac

		[ -n "$_MENU1" ] && break 
		done

}
