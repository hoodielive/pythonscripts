import builtins,collections

members = set([
    m for m in inspect.getmembers(builtins)
    if not m[0].startswith('_')]) 

len(members) 

exceptions = [
        (name, obj) for (name, obj) in members
        if inspect.isclass(obj) and 
        issubclass(obj, BaseException)] 

members -= set(exceptions)

len(exceptions), len(members) 
