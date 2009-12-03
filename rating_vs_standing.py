print 'loading data...'

from data import *

print 'parsing data...'

standings = []
rankings = []

for course in all_courses:
    standings.append(getScore(course, STANDING))
    rankings.append(getScore(course, COURSE_RANKING))

print "calculating correlation coefficient..."
import numpy
fit =  numpy.polyfit(standings, rankings, 1)
print "y = %0.5fx + %0.5f" % (fit[0],fit[1])
print "r = %0.5f" % numpy.corrcoef(standings, rankings)[0][1]

print 'importing matplotlib...'

import matplotlib
matplotlib.use('pdf')
import pylab as p

print 'plotting data...'

p.plot(standings, rankings, 'bo', ms=1)
p.savefig('paper/figures/rating_vs_standing.pdf')
