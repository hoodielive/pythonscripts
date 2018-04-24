class Chainmap(collections.MutableMapping):

    def __init__(self, maps):
        self.maps = list(maps) 
        self._keys = set() 
        for m in self.maps: self._keys.update(m) 

    def __len__(self): 
        return len(self.keys) 

    def __iter__(self): 
        return iter(self.keys)
  
    def __getitem__(self, key):
        if key not in self._keys: 
            raise KeyError(key)
        for m in self.maps:
            try: return m[key]
            except KeyError: 
                pass
   
   def __setitem__(self, key, value)
        self.maps[0][key] = value 
        self._keys.add(key)
    
    def __delitem__(self, key)
        del self.maps[0][key]
        self._keys = set() 
        for m in self.maps:
            self._keys.update(m) 

