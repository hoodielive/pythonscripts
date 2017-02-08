[?1000h[?1049h[?1h=[?2004h[27m[23m[m[H[2J[?25l[42;1H"-stdin-" [readonly] 9017L, 234002C[1;42r[?12;25h[?12l[?25h[27m[23m[m[H[2J[2;1HREV 2f36672b7d36de56c16a1bda40819dce09cfb34b
[34m#scripts[m

REV c963b3b81271abdcc4254efd6b8ecd97499933b3
[34m#scripts
#!/bin/bash 
# inpath--Verifies that a sepcified program is either valid as is or can be found in the PATH directory list [m

in_path()
{[12;9H[34m# Given a command and the PATH, tries to find the command. Returns 0 if found and executable; 1 if not. Note that this temporarily modifies[13;9H# the IFS (internal field separator) but restores it upon completion.[m[15;9Hcmd=$1 ourpath=$2 result=1[16;9HoldIFS=$IFS IFS=[31m":"[m[18;9Hfor directory in [31m"$ourpath"[m[19;9Hdo[20;17Hif [ -x $directory/$cmd ] ; then[21;25Hresult=0 [34m# If we're here, we found the command. [m[22;17Hfi[24;9Hdone[26;9HIFS=$oldIFS[27;9Hreturn $result
}


checkForCmdInPath()
{[33;9Hvar=$1[34;9Hif [ [31m"$var"[m != [31m""[m ] ; then[35;17Hif [ [31m"${var%${var#?}}"[m = [31m"/"[m ] ; then[36;25Hif [ ! -x $var ] ; then[37;33Hreturn 1[38;25Hfi[39;17Helif ! in_path $var [31m"$PATH"[m ; then[40;25Hreturn 2[41;17Hfi[42;133H1,0-1[9CTop]2;[No Name] = - VIM]1;[No Name]"-stdin-" [readonly] 9017L, 234002C[42;133H[K[42;133H1,0-1[9CTop[1;1H[?12l[?25h[?25l[42;123H^X[1;1H[42;1H[31mW10: Warning: Changing a readonly file[m[42;123H[K[?1000l[?1000h[1;1H[?12l[?25h[?25l[42;1HType  :quit<Enter>  to exit Vim[42;32H[K[42;133H1,0-1[9CTop[1;1H[?12l[?25h[?25l[42;133H[K[42;133H1,0-1[9CTop[1;1H[?12l[?25h[?25l[42;133H[K[42;133H1,0-1[9CTop[1;1H[?12l[?25h[?25l[42;123H^D[1;1H[42;123H  [6;9H[1;41r[1;1H[20M[1;42r[22;9Hfi
}


if [ $# -ne 1 ] ; then[27;9Hecho [31m"Usage: $0 command"[m >&2[28;9Hexit 1
fi

checkForCmdInPath [31m"$1"[m
case $? in[33;9H0 ) echo [31m"$1 found in PATH"[m ;;[34;9H1 ) echo [31m"$1 not found or not executable"[m ;;[35;9H2 ) echo [31m"$1 not found in PATH"[m ;;
esac

exit 0

REV d07a6c179dc4d441c1db759d7007f9a97086b7c7
[34m#scripts[m[42;1H[K[42;133H26,2-9[9C0%[6;9H[?12l[?25h[?25l[42;123H^D[6;9H[42;123H  [6;1H[1;41r[1;1H[20M[1;42r[22;1H4/5/2014 13:34,Apples,73[34m^M[m
4/5/2014 3:41,Cherries,85[34m^M[m
4/6/2014 12:46,Pears,14[34m^M[m
4/8/2014 8:59,Oranges,52[34m^M[m
4/10/2014 2:07,Apples,152[34m^M[m
4/10/2014 18:10,Bananas,23[34m^M[m
4/10/2014 2:40,Strawberries,98[34m^M
#!/bin/bash 
# inpath--Verifies that a sepcified program is either valid as is or can be found in the PATH directory list [m

in_path()
{[34;9H[34m# Given a command and the PATH, tries to find the command. Returns 0 if found and executable; 1 if not. Note that this temporarily modifies[35;9H# the IFS (internal field separator) but restores it upon completion.[m[37;9Hcmd=$1 ourpath=$2 result=1[38;9HoldIFS=$IFS IFS=[31m":"[m[40;9Hfor directory in [31m"$ourpath"[m[41;9Hdo[42;133H[K[42;133H46,1[11C0%[6;1H[?12l[?25h[?25l[42;123H^D[6;1H[42;123H  [6;1H[1;41r[1;1H[20M[1;42r[22;17Hif [ -x $directory/$cmd ] ; then[23;25Hresult=0 [34m# If we're here, we found the command. [m[24;17Hfi[26;9Hdone[28;9HIFS=$oldIFS[29;9Hreturn $result
}


checkForCmdInPath()
{[35;9Hvar=$1[36;9Hif [ [31m"$var"[m != [31m""[m ] ; then[37;17Hif [ [31m"${var%${var#?}}"[m = [31m"/"[m ] ; then[38;25Hif [ ! -x $var ] ; then[39;33Hreturn 1[40;25Hfi[41;17Helif ! in_path $var [31m"$PATH"[m ; then[42;133H[K[42;133H66,1[11C0%[6;1H[?12l[?25h[42;1H[?1000l[?2004l[?1l>[?1049lVim: Error reading input, exiting...
Vim: Finished.
[42;1H]2;tamauri@damoor: ~/Documents/uploads/scripts]1;tamauri@damoor: ~/Documents/uploads/scriptsVim: Reading from stdin...
