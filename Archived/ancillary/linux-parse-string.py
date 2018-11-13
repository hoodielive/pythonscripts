line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')

for elems in uname,*fields, homedir, sh = line.split(':'):
    print(elems) 


