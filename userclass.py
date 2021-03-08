import datetime as dt
from qreq import getuser_full, getgraph

class QuaverUserInfo(object):
    def __init__(self, dct):
        self.raw = dct
        self.id = dct['id']
        self.steam_id = dct['steam_id']
        self.username = dct['username']
        self.country = dct['country']
        self.time_registered = dct['time_registered']
        self.allowed = bool(dct['allowed'])
        self.privileges = dct['privileges']
        self.usergroups = dct['usergroups']
        self.mute_endtime = dct['mute_endtime']
        self.latest_activity = dct['latest_activity']
        self.country = dct['country']
        self.online = dct['online']

class QuaverUserRank(object):
    def __init__(self, id, mode):
        self.call_id = id
        self.raw4k = None
        self.raw7k = None
        self.stats4k = None
        self.stats7k = None
        self.update(mode)

    def update(self, mode):
        if (mode == 1 or mode == 0):
            self.raw4k = getgraph(self.call_id,mode)
            self.stats4k = self.raw4k['statistics']
        if (mode == 2 or mode == 0):
            self.raw7k = getgraph(self.call_id,mode)
            self.stats7k = self.raw7k['statistics']

class QuaverUserStats(object):
    def __init__(self, dct):
        self.raw = dct
        self.globalRank = dct['globalRank']
        self.countryRank = dct['countryRank']
        self.multiplayerWinRank = dct['multiplayerWinRank']
        self.total_score = dct['stats']['total_score']
        self.ranked_score = dct['stats']['ranked_score']
        self.overall_accuracy = dct['stats']['overall_accuracy']
        self.overall_performance_rating = dct['stats']['overall_performance_rating']
        self.play_count = dct['stats']['play_count']
        self.fail_count = dct['stats']['fail_count']
        self.max_combo = dct['stats']['max_combo']
        self.replays_watched = dct['stats']['replays_watched']
        self.total_marv = dct['stats']['total_marv']
        self.total_perf = dct['stats']['total_perf']
        self.total_great = dct['stats']['total_great']
        self.total_good = dct['stats']['total_good']
        self.total_okay = dct['stats']['total_okay']
        self.total_miss = dct['stats']['total_miss']
        self.total_pauses = dct['stats']['total_pauses']
        self.multiplayer_wins = dct['stats']['multiplayer_wins']
        self.multiplayer_losses = dct['stats']['multiplayer_losses']
        self.multiplayer_ties = dct['stats']['multiplayer_ties']

class QuaverAPIUser(object):
    def __init__(self, id):
        self.call_id = id
        self.call_time = None
        self.info = None
        self.rank = None
        self.stats4k = None
        self.stats7k = None
        self.raw = None
        self.update()
    
    def update(self):
        self.call_time = dt.datetime.now().isoformat()
        self.raw = getuser_full(self.call_id)
        self.info = QuaverUserInfo(self.raw['user']['info'])
        self.stats4k = QuaverUserStats(self.raw['user']['keys4'])
        self.stats7k = QuaverUserStats(self.raw['user']['keys7'])

    def updaterank(self, mode = 0):
        self.rank = QuaverUserRank(self.call_id, mode)

    def updateall(self):
        self.update()
        self.updaterank()

def QuaverUserGet(id):
    """
    Creates an object class inherited from the Quaver API
    """
    return(QuaverAPIUser(id))
