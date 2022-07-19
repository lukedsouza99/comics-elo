import pandas as pd
import random

class ComicAccess():

    csv = pd.read_csv(r'comic_rating.csv')

    def getRandomComic(self):
        random_comic = self.csv.iloc[random.randint(0,self.csv.shape[0]-1)]
        return random_comic


