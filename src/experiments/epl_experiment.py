"""
In this experiment we work with matches from the last 10 years in the English Premier League. 
The experiment moves along the timeline and for each timestamp it trains a model over all games before this timeline. Then it predicts scores for the games in that timestanp, 
typically 10 matches per week. The experiment's output is an array of accuracy scores that can be summarized to a single score depending who running this experiment.
"""

import numpy as np
from typing import List

from src.dataset_builder.dataset_builder import DatasetBuilder
from src.model_factory.model_factory import ModelFactory
from src.models.match import Match
from src.data_manager.data_manager import DataManager

class EPLExperiment():

    def __init__(self, dm: DataManager, ds_builder: DatasetBuilder, model_factory: ModelFactory):
        self.dm = dm
        self.ds_builder = ds_builder
        self.model_factory = model_factory


    def create_match_batches(self, matches) -> List[List[Match]]:
        pass

    def run(self) -> List[float]:
        accuracies = []
        matches = self.dm.get_matches(league='EPL', validity=10)
        batches = self.create_match_batches(matches)
        for i in range(1, len(batches)):
            model = self.model_factory.get_model()
            x_train, y_train = self.ds_builder(batches[:i])
            x_test, y_test = self.ds_builder(batches[i])
            model.fit(x_train, y_train)
            predictions = model.predict(x_test)
            accuracy = np.sum(predictions == y_test) / len(predictions)
            accuracies.append(accuracy)
        return accuracies
