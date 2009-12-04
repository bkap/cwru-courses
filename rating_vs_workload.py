from data import *
import numpy
import matplotlib
matplotlib.use('pdf')
import pylab as p

standings = []
rankings = []

for course in all_courses:
    if(int(course['coursename'][4:]) >= 400):
        continue
    if getScore(course, COURSE_RANKING) > -1.0:
        standings.append(getScore(course, WORKLOAD))
        rankings.append(getScore(course, COURSE_RANKING))

print "calculating correlation coefficient..."
import math
mstand = sum(standings) / len(standings)

fit =  numpy.polyfit(standings, rankings, 1)
print "y = %0.5fx + %0.5f" % (fit[0],fit[1])
r = numpy.corrcoef(standings, rankings)[0][1]
print "r = %0.5f" % r
def err(x,y) :
    exp = fit[0] * x + fit[1]
    return (y-exp)**2
stderr =  math.sqrt(sum(err(x,y) for x,y in
zip(standings,rankings)) / (len(standings) - 2))

p.title('Overall Rating vs Workload Rating')
p.xticks(STANDING_VALUES, WORKLOAD_LABELS, fontsize=10)
p.yticks(RATING_VALUES, RATING_LABELS, fontsize=10)
p.plot(standings, rankings, 'k,', ms=1, alpha=0.2)
l = p.plot([0.0, 4.0], [fit[1], fit[1] + 4.0*fit[0]], 'r-')
prop = matplotlib.font_manager.FontProperties(size=10)
p.legend((l,), ('y=%0.3fx+%0.5f, r=%0.5f, stderr=%0.5f' % (fit[0], fit[1], r,
stderr),), 'lower right', prop=prop)
p.savefig('paper/figures/rating_vs_workload.pdf')

import subprocess
subprocess.call(['open', 'paper/figures/rating_vs_workload.pdf'])
