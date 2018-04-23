line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

lines = uname, *fields, homedir, sh = line.split(':')

lines = dict(lines) 
print(type(lines)) 


#for instances in enumerate(lines):
#    print(lines) 


