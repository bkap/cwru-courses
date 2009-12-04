from average_time_plot import plot
from data import *

import subprocess

stuff_to_plot = (
    (WORKLOAD, 'workload_over_time', 'Average Workload', WORKLOAD_LABELS),
    (PACE, 'pace_over_time', 'Average Pace', PACE_LABELS),
    ((6,ranking), 'english_over_time', 'Average Instructor English'),
    ((7,ranking), 'expectations_over_time', 'Average Clear Expectations'),
    ((8,ranking), 'procedures_over_time', 'Average Explained Procedures'),
    ((9,ranking), 'motivation_over_time', 'Average Motivation'),
    ((10,ranking), 'questions_over_time', 'Average Encouraged Questions'),
    ((11,ranking), 'critthink_over_time', 'Average Critical Thinking'),
    ((12,ranking), 'atmosphere_over_time', 'Average Atmosphere'),
    ((13,ranking), 'prog_info_over_time', 'Average Progress Info'),
    ((14,ranking), 'fair_grading_over_time', 'Average Grading Fairness'),
    ((15,ranking), 'assistance_over_time', 'Average Available Assistance'),
    ((16,ranking), 'textbook_over_time', 'Average Textbook Usefulness'),
    ((17,ranking), 'rating_over_time', 'Average Course Rating'),
    ((18,ranking), 'instructor_over_time', 'Average Instructor Rating'),
    ((19,ranking), 'ta_over_time', 'Average TA Rating'),
    ((20,ranking), 'lab_over_time', 'Average Lab Rating'),
)

for args in stuff_to_plot:
    #plot() returns the file path
    subprocess.call(['open', plot(*args)])
