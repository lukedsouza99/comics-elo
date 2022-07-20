import pandas as pd
import random

class ComicAccess():

    csv = pd.read_csv(r'comic_rating.csv')

    def saveCsv(self):
        self.csv.to_csv(r'comic_rating.csv', header = True, index = False)

    def getRandomComic(self):
        random_comic = self.csv.iloc[random.randint(0,self.csv.shape[0]-1)]
        return random_comic


    def updateElo(self, index, elo):
        self.csv.loc[index,"Score"] = elo
        self.saveCsv()
    

    def addNew(self,title,writer,artist,year,issues,score):
        new_row =pd.DataFrame({"Title":[title],"Writer":[writer],"Artist":[artist],"Year":[year],"Issues":[issues],"Score":[score]})
        self.csv = pd.concat([self.csv, new_row], axis = 0, ignore_index = True)
        print(self.csv)
        self.saveCsv()

