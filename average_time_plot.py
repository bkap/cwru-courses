from data import *
from easy_plot import *
import pylab as p
import matplotlib.pyplot as pyplot

def plot(score_by=COURSE_RANKING, file_name='something_over_time', title='Something Over Time', ylabels=RATING_LABELS):
    p.cla()
    
    #Y
    avgs = lambda f: semester_averages(filter_semesters(semesters, f), score_by=score_by)
    artsci_avgs, artsci_errs = avgs(ARTS_AND_SCIENCES)
    engr_avgs, engr_errs = avgs(ENGINEERING)
    sages_avgs, sages_errs = avgs(SAGES)
    bus_avgs, bus_errs = avgs(WEATHERHEAD)
    # mandel_avgs, mandel_errs = avgs(MANDEL)

    file_path = 'paper/figures/%s.pdf' % file_name

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

    colors = ('r','g','b', 'c')

    fig = pyplot.figure()

    p.title(title)
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
    p.yticks(RATING_VALUES, ylabels, fontsize=10)

    lines = []
    for i in range(len(data_sets)):
        local_sem_vals = SEMESTER_VALUES[-len(data_sets[i][0]):]
        lines.append(p.errorbar(local_sem_vals, data_sets[i][0], 
                                yerr=data_sets[i][1], 
                                fmt='%so' % colors[i], ms=1))
        plot_fit(local_sem_vals, data_sets[i][0], '%s-' % colors[i])
    p.legend([l[2] for l in lines], titles, 'lower left')

    p.savefig(file_path)
    return file_path
