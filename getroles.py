#!/usr/bin/env python

hostnames = (
	'dca-cor-7609-r1',
	'dca-cor-7609-r2',
	'dca-cor-7609-r3',
	'dca-cor-7609-r4',
	'iad-tra-mx80-r1',
	'iad-tra-mx80-r2'
)

def get_role_by_hostname(hostname):
	info = {}
	info['location'] = hostname.split('-')[0]
	info['role'] = hostname.split('-')[1]
	info['model'] = hostname.split('-')[2]
	return info 

for h in hostnames:
	info = get_role_by_hostname(h)
	print('hostname: {}'.format(h))
	print('location: {}'.format(info['location']))
	print('role: {}'.format(info['role']))
	print('model: {}'.format(info['model']))

