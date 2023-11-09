class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return ("%s%s%s%s%s%s%s" % (f"{self.name:20}",
                                    f"{self.team:5}",
                                    f"{self.goals:>3}",
                                    " + ",
                                    f"{self.assists:<3}", 
                                    " = ", 
                                    f"{self.assists+self.goals}")
                )
