from data import *

orphans = set()
for course in all_courses:
    cn = course['coursename'][:4]
    if     cn not in ENGINEERING \
       and cn not in SAGES \
       and cn not in ARTS_AND_SCIENCES \
       and cn not in WEATHERHEAD \
       and cn not in MEDICAL \
       and cn not in MANDEL \
       and cn not in KNOWN_ORPHAN:
        orphans.add(cn)
print orphans