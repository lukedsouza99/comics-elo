
class Activities():


    
    def randomComicCompare(self, comicAccess, eloMaths):
        randomComicOne = comicAccess.getRandomComic()
        while True:
            randomComicTwo = comicAccess.getRandomComic()
            if randomComicOne.name != randomComicTwo.name:
                break

        print(randomComicOne)
        print("\n")
        print(randomComicTwo)
        print("\n")
        
        while True:
            answer = input("Which is better? [1/2]")
            if answer == "1":
                win = [1,0]
                break
            if answer == "2":
                win = [0,1]
                break
            print("Not an option, try again")
        
        new_values = eloMaths.updateEloScores(randomComicOne['Score'], randomComicTwo['Score'], win)
        comicAccess.updateElo(randomComicOne.name, new_values[0])
        comicAccess.updateElo(randomComicTwo.name, new_values[1])
        print(new_values)
        print(comicAccess.csv)

        
        







