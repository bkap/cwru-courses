print 'loading data...'
from data import *

print 'calculating averages...'
from easy_plot import *

#Y
avgs = lambda f: semester_averages(filter_semesters(semesters, f))
print 'a'
artsci_avgs, artsci_errs = avgs(ARTS_AND_SCIENCES)
print 'e'
engr_avgs, engr_errs = avgs(ENGINEERING)
print 's'
sages_avgs, sages_errs = avgs(SAGES)
# bus_avgs, bus_errs = avgs(WEATHERHEAD)
# mandel_avgs, mandel_errs = avgs(MANDEL)

data_sets = [
    (artsci_avgs, artsci_errs),
    (engr_avgs, engr_errs),
    (sages_avgs, sages_errs),
    # (bus_avgs, bus_errs),
    # (mandel_avgs, mandel_errs),
]

titles = [
    'Arts and Sciences',
    'Engineering',
    'SAGES',
    # 'Weatherhead',
    # 'Mandel'
]

colors = ('r','g','b')

import pylab as p
import matplotlib.pyplot as pyplot

print 'plotting data...'

fig = pyplot.figure()

p.title('Average School Ratings Over Time')
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

lines = []
for i in range(len(data_sets)):
    local_sem_vals = SEMESTER_VALUES[-len(data_sets[i][0]):]
    lines.append(p.errorbar(local_sem_vals, data_sets[i][0], 
                            yerr=data_sets[i][1], 
                            fmt='%so' % colors[i], ms=1))
    plot_fit(local_sem_vals, data_sets[i][0], '%s-' % colors[i])
p.legend([l[2] for l in lines], titles)

p.savefig('paper/figures/artsci_over_time.pdf')

import subprocess
subprocess.call(['open', 'paper/figures/artsci_over_time.pdf'])