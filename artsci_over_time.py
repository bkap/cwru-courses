import math

print 'loading data...'

from data import *

print 'computing averages...'

import numpy

averages = {}
for name, items in semesters.iteritems():
    averages[name] = numpy.average([getScore(course, COURSE_RANKING) for course in items])

print 'computing errors...'

errors = {}
for name in semesters.keys():
    std_dev = 0.0
    for course in semesters[name]:
        std_dev += (getScore(course, COURSE_RANKING) - averages[name])**2
    std_dev = math.sqrt(std_dev/len(semesters[name]))
    errors[name] = std_dev/math.sqrt(len(semesters[name]))

#Y
average_values = [averages[sem] for sem in SORTED_SEM_NAMES]
#error
errors = [errors[sem] for sem in SORTED_SEM_NAMES]

print 'importing matplotlib...'

import matplotlib
matplotlib.use('pdf')
import pylab as p
import matplotlib.pyplot as pyplot

print 'calculating fit...'

import numpy
fit =  numpy.polyfit(SEMESTER_VALUES, average_values, 1)

print 'plotting data...'

fig = pyplot.figure()

p.title('College of Arts and Sciences Rating Over Time')
ax = fig.add_subplot(111)
ax.set_autoscale_on(False)
p.ylim(0.0, 4.0)

#X axis labels
i = 0
x_values = []
x_labels = []
for i in range(len(SORTED_SEM_NAMES)):
    if i % 2 == 0:
        x_values.append(SEMESTER_VALUES[i])
        x_labels.append(SORTED_SEM_NAMES[i])
    i += 1
p.xticks(x_values, x_labels, fontsize=10)

#Y axis labels
p.yticks(RATING_VALUES, RATING_LABELS, fontsize=10)

# p.plot(SEMESTER_VALUES, average_values, 'bo')
p.plot([0.0, SEMESTER_VALUES[-1]], [fit[1], fit[1] + SEMESTER_VALUES[-1]*fit[0]], 'r-')
p.errorbar(SEMESTER_VALUES, average_values, yerr=errors, fmt='ro', ms=1)

p.savefig('paper/figures/artsci_over_time.pdf')

import subprocess
subprocess.call(['open', 'paper/figures/artsci_over_time.pdf'])