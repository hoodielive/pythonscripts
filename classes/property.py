class property:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset 
        self.fdel = fdel 

    def __get__(self, instance, owner):
        if instance is None:
            return self 
        elif self.fget is None:
            raise AttributeError("unreadable attribute")
        else:
            return self.fget(instance)

    def __set__(self, instance, value): 
        if self.fset is None:
            raise AttributeError("can't set attribute")
        else:
            self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        else:
            self.fdel(instance)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


