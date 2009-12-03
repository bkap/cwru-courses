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
#pprint.pprint(year_scores)
engineering = []
for course in SCHOOL_OF_ENGINEERING :
    if course in course_codes :
        engineering.extend(course_codes[course])
artsci = []
for course in ARTS_AND_SCIENCES :
    if course in course_codes :
        artsci.extend(course_codes[course])

sages = []

not_sages = []
for code, courses in course_codes.iteritems() :
    if code in SAGES :
        sages.extend(courses)
    else :
        not_sages.extend(courses)

for type in [COURSE_RANKING, DIFFICULTY] :   
    engineering_score = getAverageScore(engineering,type)
    artsci_score = getAverageScore(artsci, type)
    import numpy
    print "engineering: %0.5f, %d, %0.5f" % (engineering_score,
    len(engineering), numpy.std([getScore(x,type) for x in engineering]))
    print "artsci: %0.5f, %d, %0.5f" % (artsci_score, len(artsci),
    numpy.std([getScore(x,type) for x in artsci]))

    sages_scores = [getScore(x,type) for x in sages]
    not_sages_scores = [getScore(x,type) for x in not_sages]
    sages_average = getAverageScore(sages,type)
    not_sages_average = getAverageScore(not_sages,type)
    print "sages: %0.5f, %0.5f, %d" % (sages_average,
    numpy.std(sages_scores),len(sages_scores))
    print "not sages: %0.5f, %0.5f, %d" % (not_sages_average,
    numpy.std(not_sages_scores),len(not_sages_scores))
