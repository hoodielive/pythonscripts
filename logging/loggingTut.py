#!/usr/bin/env python3

import logging
import auxiliary_module

# create logger with 'spam_applications'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages 
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level 
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to handlers 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger 
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary') 

a = auxillary_module.Auxiliary()

logger.info('created an instance of auxiliary_module.Auxiliary') 
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
