#!/usr/bin/env python

import cPickle

EVALS = "evals.pickle"

STANDING = ('standing',{'freshman':1,'sophomore':2,'junior':3, 'senior':4, 'graduate':5})

ranking = {'SA':5,'A':4,"M":3,'D':2,"SD":1}
COURSE_RANKING = (17,ranking)
INSTRUCTOR_RANKING = (18,ranking)
INSTRUCTOR_ENGLISH = (5,ranking)


SCHOOL_OF_ENGINEERING = set(['EBME','ECES','ECHE','ECIV','ECMP','EEAP','EECS','EIND','EMAC','EMAE','EMCH','EMSE','ENGR','ESYS','EMAC','EFTS'])
SAGES = set(['USSY',"USSO","USNA","FSSY","FSNA","FSCC","FSSO"])
semesters = cPickle.load(open(EVALS,'rb'))

def getAverageScore(courses,criteria) :
    total = 0.
    na = 0
    for course in courses:
       score =  getScore(course,criteria) 
       if not score :
            na += 1
       else :
            total += score
    return total / (len(courses) - na)


def getScore(course, criteria) :
    total = 0.
    students = 0
    if criteria[0] not in course :
        return 0
    stat = course[criteria[0]]
    for key,value in criteria[1].items() :
        students += stat[key]
        total += stat[key] * value
   
    if students == 0 :
        return 0
    return total/students

course_codes = dict()
all_courses =  []
for sem,semester in semesters.items() :
    for course in semester :
        if(course['coursename'] == 'EMSE203' and 17 not in course) : print(sem)
        all_courses.append(course)

for course in all_courses :
    code = course['coursename'][:4]
    if('O' in course['coursename'][4:]) :
        #print(course['coursename'])
        course['coursename'] = code + course['coursename'][4:].replace("O","0")
    try :
        if(int(course['coursename'][4:]) >= 400) :
            continue
    except ValueError as e:
        print(course)
        import sys
        sys.exit(1)
    if code not in course_codes :
        course_codes[code] = [course]
    else :
        course_codes[code].append(course)

department_ratings = {}
for code in course_codes :
    department_ratings[code] =  (getAverageScore(course_codes[code],COURSE_RANKING),len(course_codes[code]))
year_scores = {}
for sem in semesters:
    year_scores[sem] = (getAverageScore(semesters[sem],COURSE_RANKING),len(semesters[sem]))

import pprint

pprint.pprint(department_ratings)
pprint.pprint(year_scores)
