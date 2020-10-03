import datetime

class Match():

    def __init__(self, home_team: str, away_team: str, home_goals: int, away_goals: int, start_time: datetime.datetime):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.start_time = start_time
