import pdb 
pdb.set_trace() 


class TableA(object): pass
class TableB(object): pass
class TableC(object): pass

class Poller(object):
    TABLES = { TableA: '1',
               TableB: '2', 
               TableC: '3'} 

    def poll(self):
        for table, value in self.TABLES.iteritems(): 
            print(table) 
            return 


p = Poller() 
p.poll() 
