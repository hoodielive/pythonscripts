#!/usr/bin/env python3

import shelve
import apache_log_parser

logfile = open('/var/log/apache2/access.log', 'r')

shelve_file = shelve.open('access.s')

for line in logfile:
	d_line = apache_log_parser.dictify_logline(line)
	shelve_file[d_line['remote_host']] = shelve_file.setdefault(d_line['remote_host'], 0) + \
		int(d_line['bytes_sent'])

logfile.close()
shelve_file.close()