#!/usr/bin/env python

from data import *

department_ratings = {}
for code in course_codes :
    department_ratings[code] =  (getAverageScore(course_codes[code],COURSE_RANKING),len(course_codes[code]))
year_scores = {}
for sem in semesters:
    year_scores[sem] = (getAverageScore(semesters[sem],COURSE_RANKING),len(semesters[sem]))

import pprint

#pprint.pprint(department_ratings)
#pprint.pprint(year_scores)
for type in [DIFFICULTY, COURSE_RANKING] :
    engineering = []
    for course in SCHOOL_OF_ENGINEERING :
        if course in course_codes :
            engineering.extend(course_codes[course])
    engineering_score = getAverageScore(engineering,type)
    artsci = []
    for course in ARTS_AND_SCIENCES :
        if course in course_codes :
            artsci.extend(course_codes[course])
    artsci_score = getAverageScore(artsci, type)
    import numpy
    print "engineering: %0.5f, %d, %0.5f" % (engineering_score,
    len(engineering), numpy.std([getScore(x,type) for x in engineering]))
    print "artsci: %0.5f, %d, %0.5f" % (artsci_score, len(artsci),
    numpy.std([getScore(x,type) for x in artsci]))

