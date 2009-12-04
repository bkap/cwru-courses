import scatter_plot
from data import *

scatter_plot.plot(x_scoring=STANDING, x_labels=STANDING_LABELS, y_scoring=COURSE_RANKING, y_labels=RATING_LABELS, filename='rating_vs_standing', title='Overall Rating vs University Standing')
