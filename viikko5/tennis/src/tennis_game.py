class PointCounter:

    def __init__(self, player1_name, player2_name):
        self.total = 0
        self.table = {player1_name: 0, player2_name: 0}
    
    def increase(self, player_name):
        print("add point to ",player_name)
        self.table[player_name]+=1
        self.total += 1
        if self.total > 7:
            self.total = 6
            for player in self.table.keys():
                self.table[player]-=1
        
    def get_score(self, player_name):
        return self.table[player_name]
    
    
class StateNamer:
    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.state_names = [
            ["Love-All",                  "Love-Fifteen",             "Love-Thirty",              "Love-Forty",                 "Win for "+self.p2_name],
            ["Fifteen-Love",              "Fifteen-All",              "Fifteen-Thirty",           "Fifteen-Forty",              "Win for "+self.p2_name],
            ["Thirty-Love",               "Thirty-Fifteen",           "Thirty-All",               "Thirty-Forty",               "Win for "+self.p2_name],
            ["Forty-Love",                "Forty-Fifteen",            "Forty-Thirty",             "Deuce",                      "Advantage "+self.p2_name],
            ["Win for "+self.p1_name,     "Win for "+self.p1_name,    "Win for "+self.p1_name,    "Advantage "+self.p1_name,    "Deuce"]
        ]
    
    def get_state_name(self, p1_score, p2_score):
        return self.state_names[p1_score][p2_score]


class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.counter = PointCounter(player1_name, player2_name)
        self.state_namer = StateNamer(player1_name, player2_name)

    def won_point(self, player_name):
        self.counter.increase(player_name)

    def get_score(self):
        return self.state_namer.get_state_name(
            self.counter.get_score(self.player1_name),
            self.counter.get_score(self.player2_name)
        )
        