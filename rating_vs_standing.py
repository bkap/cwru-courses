print 'loading data...'

from data import *

print 'parsing data...'

standings = []
rankings = []

with open('ratings_standings.csv', 'w') as f:
    for course in all_courses:
        standings.append(getScore(course, STANDING))
        rankings.append(getScore(course, COURSE_RANKING))
        # f.write("%s, %s\n" % (getScore(course, STANDING), getScore(course, COURSE_RANKING)))

print "calculating correlation coefficient..."
import numpy

print numpy.corrcoef(standings, rankings)

print 'importing matplotlib...'

import pylab as p

print 'plotting data...'

p.plot(standings, rankings, 'bo', ms=1)
p.show()
