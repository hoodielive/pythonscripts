def create_unbound_local_var_error():
    print('In this test == ', x) 
    x = 3

create_unbound_local_var_error()

create_unbound_local_var_error.__code__
create_unbound_local_var_error.__code__.co_argcount
create_unbound_local_var_error.__code__.co_name
create_unbound_local_var_error.__code__.co_names
create_unbound_local_var_error.__code__.co_locals
create_unbound_local_var_error.__code__.co_varnames

import dis

dis.dis(create_unbound_local_var_error.co_code) 
