"""
This script was used to help us sort subject codes into categories. It was not used to generate any statistical data.
"""

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

hard = []
soft = []

for code in sorted(subject_codes.keys()):
    hs = 'x'
    while hs != 'h' and hs != 's' and hs != 'i':
        hs = raw_input(code)
        if hs == 'h':
            hard.append(code)
        elif hs == 's':
            soft.append(code)

print hard
print soft