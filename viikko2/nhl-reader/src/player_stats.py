class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        return [p for p in self.reader.read() if p.nationality == nat]