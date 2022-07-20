import EloMaths as EM
import ComicAccess
import Activities

kFactor = 16
eloMaths = EM.EloMaths(kFactor)
activities = Activities.Activities()
comicAccess = ComicAccess.ComicAccess()


activities.randomComicCompare(comicAccess, eloMaths)

  

