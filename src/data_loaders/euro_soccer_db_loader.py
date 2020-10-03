import sqlite3
import pandas as pd

from src.data_loaders.data_loader import DataLoader

class EuroSoccerDatabaseLoader(DataLoader):

	def __init__(self):
		self.cnx = sqlite3.connect('../../European Soccer Database/database.sqlite')


	def load_countries(self):
		df = pd.read_sql("SELECT * FROM Country", self.cnx)
		return df

	def load_leagues(self):
		df = pd.read_sql("SELECT * FROM League", self.cnx)
		return df

	def load_matches(self):
		df = pd.read_sql("SELECT * FROM Match", self.cnx)
		return df
	
	def load_players(self):
		df = pd.read_sql("SELECT * FROM Player", self.cnx)
		return df
	
	def load_player_attributes(self):
		df = pd.read_sql("SELECT * FROM Player_Attributes", self.cnx)
		return df

	def load_teams(self):
		df = pd.read_sql("SELECT * FROM Team", self.cnx)
		return df
	
	def load_team_attributes(self):
		df = pd.read_sql("SELECT * FROM Team_Attributes", self.cnx)
		return df
