import matplotlib
matplotlib.use('pdf')
import math
import numpy
import pylab as p
from data import SORTED_SEM_NAMES, getScore, COURSE_RANKING

def filter_semesters(semesters, filter_list):
    new_semesters = {}
    for name, items in semesters.iteritems():
        for course in items:
            if course['coursename'][:4] in filter_list:
                if not new_semesters.has_key(name): new_semesters[name] = []
                new_semesters[name].append(course)
    return new_semesters

def semester_averages(semesters):
    averages = {}
    for name, items in semesters.iteritems():
        averages[name] = numpy.average([getScore(course, COURSE_RANKING) for course in items])
    
    errors = {}
    for name in semesters.keys():
        std_dev = 0.0
        for course in semesters[name]:
            std_dev += (getScore(course, COURSE_RANKING) - averages[name])**2
        std_dev = math.sqrt(std_dev/len(semesters[name]))
        errors[name] = std_dev/math.sqrt(len(semesters[name]))
    filtered_names = sorted(semesters.keys())
    return [averages[sem] for sem in filtered_names], [errors[sem] for sem in filtered_names]

def plot_fit(x, y, style='r-'):
    fit =  numpy.polyfit(x, y, 1)
    p.plot([x[0], x[-1]], [fit[1] + x[0]*fit[0], fit[1] + x[-1]*fit[0]], style)
