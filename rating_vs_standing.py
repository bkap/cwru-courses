from data import *
from scipy import stats
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
        standings.append(getScore(course, STANDING))
        rankings.append(getScore(course, COURSE_RANKING))

# fit =  numpy.polyfit(standings, rankings, 1)
# corrcoeff, prob = stats.pearsonr(standings, rankings)
r = numpy.corrcoef(standings, rankings)[0][1]

print stats.linregress(standings, rankings)
m, b, r, prob, stderr = stats.linregress(standings, rankings)
fit = (m, b)

p.title('Overall Rating vs University Standing')
p.xticks(STANDING_VALUES, STANDING_LABELS, fontsize=10)
p.yticks(RATING_VALUES, RATING_LABELS, fontsize=10)
p.plot(standings, rankings, 'k,', ms=1, alpha=0.2)
l = p.plot([0.0, 4.0], [fit[1], fit[1] + 4.0*fit[0]], 'r-')
prop = matplotlib.font_manager.FontProperties(size=10)
p.legend((l,), ('y=%0.3fx + %0.5f, r=%0.5f, stderr=0.65941' % (fit[0], fit[1], r),), 'lower right', prop=prop)
p.savefig('paper/figures/rating_vs_standing.pdf')

import subprocess
subprocess.call(['open', 'paper/figures/rating_vs_standing.pdf'])
