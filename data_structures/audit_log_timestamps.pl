sudo cat /var/log/audit/audit.log | perl -ne 'chomp; if ( /(.*msg=audit\()(\d+)(\.\d+:\d+.*)/ ) { $td = scalar localtime $2; print "$1$td$3\n"; }'
