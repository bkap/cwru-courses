#!/usr/bin/env python

from data import *
from scipy.stats import ttest_ind, tstd
department_ratings = {}

#extract data by department code
for code in course_codes :
    department_ratings[code] =  (getAverageScore(course_codes[code],COURSE_RANKING),len(course_codes[code]))
year_scores = {}
#extract data by semester
for sem in semesters:
    year_scores[sem] = (getAverageScore(semesters[sem],COURSE_RANKING),len(semesters[sem]))

import pprint

#pprint.pprint(department_ratings)
#pprint.pprint(year_scores)

#select the courses in the school of engineering
engineering = []
for course in ENGINEERING :
    if course in course_codes :
        engineering.extend(course_codes[course])

#select the courses in the college of arts and sciences
artsci = []
for course in ARTS_AND_SCIENCES :
    if course in course_codes :
        artsci.extend(course_codes[course])

#separate the sages classes from the not-sages classes
sages = []
not_sages = []
for code, courses in course_codes.iteritems() :
    if code in SAGES :
        sages.extend(courses)
    else :
        not_sages.extend(courses)


for type in [COURSE_RANKING, WORKLOAD] :   
    engineering_score = getAverageScore(engineering,type)
    engineering_scores = [getScore(x,type) for x in engineering]
    artsci_score = getAverageScore(artsci, type)
    artsci_scores = [getScore(x,type) for x in artsci]
    
    print "engineering: %0.5f, %d, %0.5f" % (engineering_score,
        len(engineering), tstd( engineering_scores))
    print "artsci: %0.5f, %d, %0.5f" % (artsci_score, len(artsci),
        tstd(artsci_scores))
    print ("T-score: engineering != artsci: t = %0.5f, p = %0.5f" %
        ttest_ind(engineering_scores, artsci_scores) )
    print ''
    sages_scores = [getScore(x,type) for x in sages]
    not_sages_scores = [getScore(x,type) for x in not_sages]
    sages_average = getAverageScore(sages,type)
    not_sages_average = getAverageScore(not_sages,type)
    print "sages: %0.5f, %0.5f, %d" % (sages_average,
    tstd(sages_scores),len(sages_scores))
    print "not sages: %0.5f, %0.5f, %d" % (not_sages_average,
    tstd(not_sages_scores),len(not_sages_scores))
    print ("T-score: sages != not sages: t = %0.5f, p= %0.5f" %
        ttest_ind(sages_scores,not_sages_scores))
    print ''
