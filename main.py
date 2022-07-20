import EloMaths as EM
import ComicAccess

kFactor = 16
eloMaths = EM.EloMaths(kFactor)

comicAccess = ComicAccess.ComicAccess()
print(comicAccess.getRandomComic())

comicAccess.updateElo(0,20)

comicAccess.addNew("Hawkeye", "Matt Fraction", "David Aja", 2017, 50, 30)

