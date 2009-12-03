from average_time_plot import plot
from data import *

import subprocess

stuff_to_plot = (
    (COURSE_RANKING, 'rating_over_time', 'Average Course Ratings Over Time'),
    (DIFFICULTY, 'difficulty_over_time', 'Average Difficulty Over Time'),
    (PACE, 'pace_over_time', 'Average Pace Over Time', PACE_LABELS),
    (INSTRUCTOR_ENGLISH, 'english_over_time', 'Average Instructor English Over Time'),
)

for args in stuff_to_plot:
    #plot() returns the file path
    subprocess.call(['open', plot(*args)])