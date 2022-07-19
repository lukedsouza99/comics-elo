
class EloMaths():


    def __init__(self, dividor, kFactor):
        self.dividor = dividor 
        self.kFactor = kFactor

    
    # Calculates probability of winning when given two ELOs.
    def probabilityOfWin(self, eloA, eloB):
        
        probabilityOfA = 1 / (1 + 10**((eloB - eloA)/self.dividor))
        return [probabilityOfA, 1 - probabilityOfA]


    # Updates ELOs using probability of winning and actual results.
    def updateScoreAssumeAWin(self,eloA, eloB, wins):

        probabilities = self.probabilityOfWin(eloA, eloB)
        print(probabilities)
        


x = EloMaths(400,16)

x.updateScoreAssumeAWin(2600,2300,1)








