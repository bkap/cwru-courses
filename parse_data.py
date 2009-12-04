"""
This is a positively monstrous (i.e. bad) script which turns course evaluation data from text files into Python objects. Format is like so:

data{
    'seasonYEAR':[  #really this is just the file name of the data
        {
            'coursename':'SUBJ999',
            'section':'probably blank',
            'instructor':'some guy',
            'count':'number of responses as a string
            'course_fit': string which is one of:
                ('major_required', 'tech_in_major', 
                'core_required', 'minor_option', 
                'open_elective'),
            'standing': string which is one of:
                ('freshman', 'sophomore', 'junior', 
                'senior', 'graduate'),
            'pace': string which is one of:
                ('very_fast', 'rather_fast', 'moderate', 
                'rather_slow', 'very_slow'),
            'work_load': string which is one of:
                ('very_heavy', 'rather_heavy', 'moderate', 
                'rather_light', 'very_light'),
            # Then I got lazy and started just referring to question number
            5: string which is one of:
                ('SA', 'A', 'M', 'D', 'SD', 'NA')
                which actually makes very little sense for questions 17-20, which
                actually ask for ('E', 'VG' 'G', 'F', 'P'),
            6: same kind of string,
            ...
            20: same kind of string
        }
    ]
}
"""

import re, cPickle

data = {
    'fall1997':[],
    'fall1998':[],
    'fall1999':[],
    'fall2000':[],
    'fall2001':[],
    'fall2002':[],
    'fall2003':[],
    'fall2004':[],
    'fall2005':[],
    'fall2006':[],
    'spring1998':[],
    'spring1999':[],
    'spring2000':[],
    'spring2001':[],
    'spring2002':[],
    'spring2003':[],
    'spring2004':[],
    'spring2005':[],
    'spring2006':[],
}

course_name = re.compile(r'^\* COURSE NAME\s+:\s+(?P<coursename>\w+)\s+SECTION:(?P<section>.+)$')
instructor = re.compile(r'^\* INSTRUCTOR\s+:\s+(?P<instructor>.+)$')

course_fit = re.compile(r'^\s+1\..+')
course_fit_opts = re.compile(r'^MAJOR REQUIRED\s*: (?P<major_required>\w+)%?\s+TECH IN MAJOR\s*: (?P<tech_in_major>\w+)%?\s+CORE REQUIRED\s*: (?P<core_required>\w+)%?\s+MINOR OPTION\s*: (?P<minor_option>\w+)%?\s+OPEN ELECTIVE\s*: (?P<open_elective>\w+)%?.*$')

standing = re.compile(r'^\s+2\..+')
standing_opts = re.compile(r'^FRESHMAN\s*:\s+(?P<freshman>\w+)%?\s+SOPHOMORE\s*:\s+(?P<sophomore>\w+)%?\s+JUNIOR\s*:\s+(?P<junior>\w+)%?\s+SENIOR\s*:\s+(?P<senior>\w+)%?\s+GRADUATE\s*:\s+(?P<graduate>\w+)%?.*$')

pace = re.compile(r'^\s+3\..+')
pace_opts = re.compile(r'^VERY FAST\s*:\s+(?P<very_fast>\w+)%?\s+RATHER FAST\s*:\s+(?P<rather_fast>\w+)%?\s+MODERATE\s*:\s+(?P<moderate>\w+)%?\s+RATHER SLOW\s*:\s+(?P<rather_slow>\w+)%?\s+VERY SLOW\s*:\s+(?P<very_slow>\w+)%?.*$')

work_load = re.compile(r'^\s+4\..+')
work_load_opts = re.compile(r'^VERY HEAVY\s*:\s+(?P<very_heavy>\w+)%?\s+RATHER HEAVY\s*:\s+(?P<rather_heavy>\w+)%?\s+MODERATE\s*:\s+(?P<moderate>\w+)%?\s+RATHER LIGHT\s*:\s+(?P<rather_light>\w+)%?\s+VERY LIGHT\s*:\s+(?P<very_light>\w+)%?.*$')

form_count = re.compile(r'^\*\* COURSE FORM COUNT :\s+(?P<count>\d+).*$')

the_rest = re.compile(r'^\s?(?P<number>\d+)\. \D+(?P<SA>\d+)\s+(?P<A>\d+)\s+(?P<M>\d+)\s+(?P<D>\d+)\s+(?P<SD>\d+)\s+(?P<NA>\d+)\s+$')

def opt_parse(this_course, f, opt_regex, groups):
    lines = ' '.join([f.next().strip(), f.next().strip()])
    opts = opt_regex.match(lines)
    return_dict = {}
    for g in groups:
        return_dict[g] = int(opts.group(g))
    return return_dict

for path in data.keys():
    with open('data/%s.txt' % path, 'r') as f:
        for line in f:
            m = course_name.match(line)
            if m:
                this_course = {
                    'coursename': m.group('coursename').strip(),
                    'section': m.group('section').strip()
                }
                data[path].append(this_course)
                continue
            m = instructor.match(line)
            if m:
                this_course['instructor'] = m.group('instructor').strip()
                continue
            if course_fit.match(line):
                this_course['course_fit'] = opt_parse(this_course, f, course_fit_opts,
                            ['major_required', 'tech_in_major', 
                            'core_required', 'minor_option', 'open_elective'])
                continue
            if standing.match(line):
                this_course['standing'] = opt_parse(this_course, f, standing_opts,
                            ['freshman', 'sophomore', 'junior', 'senior', 'graduate'])
                continue
            if pace.match(line):
                this_course['pace'] = opt_parse(this_course, f, pace_opts,
                            ['very_fast', 'rather_fast', 'moderate', 'rather_slow', 'very_slow'])
                continue
            if work_load.match(line):
                this_course['work_load'] = opt_parse(this_course, f, work_load_opts,
                            ['very_heavy', 'rather_heavy', 'moderate', 'rather_light', 'very_light'])
                continue
            m = form_count.match(line)
            if m:
                this_course['form_count'] = int(m.group('count'))
            m = the_rest.match(line)
            if m:
                n = int(m.group('number'))
                this_course[n] = {}
                for r in ['SA', 'A', 'M', 'D', 'SD', 'NA']:
                    this_course[n][r] = int(m.group(r))

with open('out.pickle', 'w') as f:
    cPickle.dump(data, f)
