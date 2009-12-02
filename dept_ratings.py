#!/usr/bin/env python

from data import *

department_ratings = {}
for code in course_codes :
    department_ratings[code] =  (getAverageScore(course_codes[code],COURSE_RANKING),len(course_codes[code]))
year_scores = {}
for sem in semesters:
    year_scores[sem] = (getAverageScore(semesters[sem],COURSE_RANKING),len(semesters[sem]))

import pprint

pprint.pprint(department_ratings)
pprint.pprint(year_scores)
