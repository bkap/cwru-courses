print 'loading data...'

from data import *

print 'parsing data...'

standings = []
rankings = []

for course in all_courses:
    if(int(course['coursename'][4:]) >= 400):
        continue
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

p.title('Overall Rating vs University Standing')
p.xticks(STANDING_VALUES, STANDING_LABELS, fontsize=10)
p.yticks(RATING_VALUES, RATING_LABELS, fontsize=10)
p.plot(standings, rankings, 'k,', ms=1, alpha=0.2)
p.plot([0.0, 4.0], [fit[1], fit[1] + 4.0*fit[0]], 'r-')
p.legend(['rating', 'regression'], 'lower right')
p.savefig('paper/figures/rating_vs_standing.pdf')

import subprocess
subprocess.call(['open', 'paper/figures/rating_vs_standing.pdf'])
