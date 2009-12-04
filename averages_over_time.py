from average_time_plot import plot
from data import *

import subprocess

stuff_to_plot = (
    (PACE, '3_pace_over_time', 'Average Pace (3)', PACE_LABELS),
    (WORKLOAD, '4_workload_over_time', 'Average Workload (4)', WORKLOAD_LABELS),
    ((5,ranking), '5_command_over_time', 'Average Instructor Command (5)'),
    ((6,ranking), '6_english_over_time', 'Average Instructor English (6)'),
    ((7,ranking), '7_expectations_over_time', 'Average Clear Expectations (7)'),
    ((8,ranking), '8_procedures_over_time', 'Average Explained Procedures (8)'),
    ((9,ranking), '9_motivation_over_time', 'Average Motivation (9)'),
    ((10,ranking), '10_questions_over_time', 'Average Encouraged Questions (10)'),
    ((11,ranking), '11_critthink_over_time', 'Average Critical Thinking (11)'),
    ((12,ranking), '12_atmosphere_over_time', 'Average Atmosphere (12)'),
    ((13,ranking), '13_prog_info_over_time', 'Average Progress Info (13)'),
    ((14,ranking), '14_fair_grading_over_time', 'Average Grading Fairness (14)'),
    ((15,ranking), '15_assistance_over_time', 'Average Available Assistance (15)'),
    ((16,ranking), '16_textbook_over_time', 'Average Textbook Usefulness (16)'),
    ((17,ranking), '17_rating_over_time', 'Average Course Rating (17)'),
    ((18,ranking), '18_instructor_over_time', 'Average Instructor Rating (18)'),
    ((19,ranking), '19_ta_over_time', 'Average TA Rating (19)'),
    ((20,ranking), '20_lab_over_time', 'Average Lab Rating (20)'),
)

for args in stuff_to_plot:
    #plot() returns the file path
    plot(*args)
    # subprocess.call(['open', ])
