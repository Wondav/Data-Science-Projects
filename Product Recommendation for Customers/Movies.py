import pandas as pd
import numpy as np
from surprise import Reader
from surprise import Dataset
from collections import defaultdict

class Movie:
    # store the paths to the files
    ratings_file = 'C:/Users/Wonder/Data-Science-Projects/Product Recommendation for Customers/data/Dataset.csv'
    movie_file = 'C:/Users/Wonder/Data-Science-Projects/Product Recommendation for Customers/data/Movie_Id_Titles.csv'

    def load_movie_ratings(self):
        self.movieID_to_name = {}
        self.name_to_movieID = {}
        # create ratings dataset
        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        ratingsDataset = Dataset.load_from_file(self.ratings_file, reader)

        file = pd.read_csv(self.movie_file)
        for index, row in file.iterrows():
            movieID = row['item_id']
            moviename = row['title']
            self.movieID_to_name[movieID] = moviename
            self.name_to_movieID[moviename] = movieID

        return ratingsDataset
    
    def getPopularityRanks(self):
        pass

    def getmovieName(self, movieId):
        if movieId in self.movieID_to_name:
            return self.movieID_to_name[movieId]
        else:
            return ""

    def getmovieId(self, movieName):
        if movieName in self.name_to_movieID:
            return self.name_to_movieID[movieName]
        else:
            return 0