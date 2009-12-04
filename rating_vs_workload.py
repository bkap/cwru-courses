import scatter_plot
from data import *

scatter_plot.plot(x_scoring=WORKLOAD, x_labels=WORKLOAD_LABELS, y_scoring=COURSE_RANKING, y_labels=RATING_LABELS, filename='rating_vs_workload', title='Overall Rating vs Workload Rating')
