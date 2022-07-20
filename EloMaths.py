
class EloMaths():


    dividor = 400

    def __init__(self, kFactor):
        self.kFactor = kFactor

    
    # Calculates probability of winning when given two ELOs.
    def probabilityOfWin(self, eloA, eloB):
        probabilityOfA = 1 / (1 + 10**((eloB - eloA)/self.dividor))
        return [probabilityOfA, 1 - probabilityOfA]


    # Updates ELOs using probability of winning and actual results.
    def updateEloScores(self,eloA, eloB, wins):
        probabilities = self.probabilityOfWin(eloA, eloB)
        updatedEloA = eloA + self.kFactor * (wins[0] - probabilities[0])
        updatedEloB = eloB + self.kFactor * (wins[1] - probabilities[1])
        return [round(updatedEloA), round(updatedEloB)]
        
        







