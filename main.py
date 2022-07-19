import EloMaths as EM
import ComicAccess

kFactor = 16
eloMaths = EM.EloMaths(kFactor)

comicAccess = ComicAccess.ComicAccess()
print(comicAccess.getRandomComic())



