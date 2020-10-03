import unittest


from src.data_loaders.euro_soccer_db_loader import EuroSoccerDatabaseLoader


class TestEuroSoccerDBLoader(unittest.Testcase):

	def setUp(self):
		self.loader = EuroSoccerDatabaseLoader()

	def test_load_countries(self):
		countries = self.loader.load_countries()
		for country in countries:
			print(country)
