from data import *

with open('ratings_standings.csv', 'w') as f:
    for course in all_courses:
        f.write("%s, %s\n" % (getScore(course, STANDING), getScore(course, COURSE_RANKING)))