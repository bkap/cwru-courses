import cPickle
from filters import *

EVALS = "evals.pickle"

STANDING_VALUES = [0.0, 1.0, 2.0, 3.0, 4.0]
RATING_VALUES = STANDING_VALUES
STANDING_LABELS = ['Freshman (0)', 'Sophomore (1)', 'Junior (2)', 'Senior (3)', 'Graduate (4)']
RATING_LABELS = ['Poor (0)', 'Fair (1)', 'Good (2)', 'Very Good (3)', 'Excellent (4)']
PACE_LABELS = ['Very Slow (0)', 'Rather Slow (1)', 'Moderate (2)', 'Rather Fast (3)', 'Very Fast (4)']
WORKLOAD_LABELS = ['Very Light (0)', 'Rather Light (1)', 'Moderate (2)', 'Rather Heavy (3)', 'Very Heavy (4)']

STANDING = ('standing', dict(freshman=0, sophomore=1, junior=2, senior=3, graduate=4))

ranking=dict(SA=4, A=3, M=2, D=1, SD=0)

WORKLOAD = ('work_load',
    dict(very_heavy=4,rather_heavy=3,moderate=2, rather_light=1, very_light=0))
PACE = ('pace',
    dict(very_fast=4, rather_fast=3, moderate=2, rather_slow=1, very_slow=0))
INSTRUCTOR_ENGLISH = (6,ranking)
COURSE_RANKING = (17,ranking)
INSTRUCTOR_RANKING = (18,ranking)

semesters = cPickle.load(open(EVALS,'rb'))

# Build list of all courses
course_codes = dict()
all_courses =  []
for sem,semester in semesters.items():
    for course in semester:
        all_courses.append(course)

# Clean course code data
for course in all_courses :
    code = course['coursename'][:4]
    if('O' in course['coursename'][4:]):
        course['coursename'] = code + course['coursename'][4:].replace("O","0")
    try :
        if(int(course['coursename'][4:]) >= 400):
            continue
    except ValueError as e:
        print(course)
        import sys
        sys.exit(1)
    if code not in course_codes :
        course_codes[code] = [course]
    else :
        course_codes[code].append(course)

SEM_NAMES = semesters.keys()
YEARS = sorted(list(set([n[-4:] for n in SEM_NAMES])))
SORTED_SEM_NAMES = []
for year in YEARS:
    for n in ['spring%s' % year, 'fall%s' % year]:
        if n in SEM_NAMES:
            SORTED_SEM_NAMES.append(n)
SEMESTER_VALMAP = {}
i = 0.0
for sem in SORTED_SEM_NAMES:
    SEMESTER_VALMAP[sem] = i
    i += 0.5
SEMESTER_VALUES = sorted(SEMESTER_VALMAP.values())

def getScore(course, criteria) :
    total = 0.
    students = 0
    if criteria[0] not in course :
        return -1
    stat = course[criteria[0]]
    for key,value in criteria[1].items() :
        students += stat[key]
        total += stat[key] * value
   
    if students == 0 :
        return -1
    return total/students

def getAverageScore(courses,criteria) :
    total = 0.
    na = 0
    for course in courses:
        score =  getScore(course,criteria) 
        if score == -1 :
             na += 1
        else :
            total += score
    return total / (len(courses) - na)
