from qreq import getserverstats

class QuaverServerInfo(object):
    def __init__(self):
        self.raw = None
        self.status = None
        self.stats = None
        self.update()
    
    def update(self):
        self.raw = getserverstats()
        self.status = self.raw['status']
        self.stats = self.raw['stats']

def QuaverServerStats():
    return(QuaverServerInfo())
