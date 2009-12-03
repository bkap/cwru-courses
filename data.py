import cPickle

EVALS = "evals.pickle"

STANDING_VALUES = [0.0, 1.0, 2.0, 3.0, 4.0]
STANDING_LABELS = ['\nFreshman', '\nSophomore', '\nJunior', '\nSenior', '\nGraduate']
RATING_VALUES = [0.0, 1.0, 2.0, 3.0, 4.0]
RATING_LABELS = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']

STANDING = ('standing', dict(freshman=0, sophomore=1, junior=2, senior=3, graduate=4))

ranking=dict(SA=4, A=3, M=2, D=1, SD=0)
COURSE_RANKING = (17,ranking)
INSTRUCTOR_RANKING = (18,ranking)
INSTRUCTOR_ENGLISH = (5,ranking)
DIFFICULTY = ('work_load',dict(very_heavy=4,rather_heavy=3,moderate=2,
rather_light=1, very_light=0))
ENGINEERING = set([
    'EBME','ECES','ECHE','ECIV',
    'ECMP','EEAP','EECS','EIND',
    'EMAC','EMAE','EMCH','EMSE',
    'ENGR','ESYS','EMAC','EFTS',
    'CMPS','ESCI','EPOM'
])
SAGES = set([
    'USSY',"USSO","USNA","FSSY",
    "FSNA","FSCC","FSSO","FSCS",
    "USFS","FSTS",
])
ARTS_AND_SCIENCES = set([
    "AMST","HSTY","ANTH","INTL"
    "ARTS","ITAL","ARAB","JAPN",
    "ASTR","LATN","BIOL","MATH",
    "CHEM","MUSC","CHIN","PHIL",
    "CHST","PHYS","CLSC","POSC",
    "COGS","PSCL","COSI","RLGN",
    "DANC","RUSN","ENGL","SOCI",
    "ETHS","SPAN","FRCH","STAT",
    "GEOL","THTR","GREK","WLIT",
    "GRMN","WMST","HBRW","WSTD",
    "ASIA","JDST","ESTD","APMU",
    "MUHI","EDUC","CMPL","ARTS",
    "GERO","LITR","MUED","MUTH",
    "ARTH","MUGN"
])
WEATHERHEAD = set([
    'ACCT', 'BAFI', 'ECON', 'LHRP', 
    'PLCY', 'MKMR', 'MIDS', 'OPMT', 
    'OPRE', 'ORBH', 'MGMT', 'HSMC',
    'EDMP', 'ENTP', 'BIOS', 'EMBA',
    'QUMM', 'BLAW', 
])
MEDICAL = set([
    'PATH','BETH','NTRN','BIOC',
])
MANDEL = set([
    'SASS',
])
KNOWN_ORPHAN = set([
    'ARSC'
])
subject_codes = {
    'ABLE': "ABILITY BASED LEARNING ENVIR     ",
    'ACCT': "ACCOUNTING                       ",
    'ACES': "ACAD & COMPUT EXCELLENCE SEM     ",
    'ADHT': "ADOLESCENT HEALTH                ",
    'AMBM': "AMBULATORY MEDICINE              ",
    'AMST': "AMERICAN STUDIES                 ",
    'ANAT': "ANATOMY                          ",
    'ANES': "ANESTHESIOLOGY                   ",
    'ANTH': "ANTHROPOLOGY                     ",
    'APMU': "APPLIED MUSIC                    ",
    'ARAB': "ARABIC                           ",
    'ARSC': "COLLEGE SCHOLARS PROGRAM         ",
    'ARTH': "ART HISTORY                      ",
    'ARTK': "COMPUTERS IN VISUAL ARTS         ",
    'ARTS': "ART STUDIO                       ",
    'ASCV': "ASIAN CIVILIZATION               ",
    'ASIA': "ASIAN STUDIES                    ",
    'ASTR': "ASTRONOMY                        ",
    'BAFI': "BANKING AND FINANCE              ",
    'BASC': "BASIC SCIENCE CURRICULUM         ",
    'BETH': "BIOETHICS                        ",
    'BIOC': "BIOCHEMISTRY                     ",
    'BIOL': "BIOLOGY                          ",
    'BIOM': "BIOMETRY                         ",
    'BIOS': "BIOSCIENCE ENTREPRENEURSHIP      ",
    'BLAW': "BUSINESS LAW                     ",
    'BOCR': "BASIS OF CLINICAL REASONING      ",
    'BSTP': "BIOMEDICAL SCIENCES TRAIN PROG   ",
    'CAPG': "CORE ACADEMIC PROGRAM            ",
    'CARD': "CARDIOLOGY                       ",
    'CARE': "PRIMARY CARE COURSES             ",
    'CBIO': "CELLULAR & MOLECULAR BIOL        ",
    'CFNU': "COMMUNITY FRONTIER NURSING       ",
    'CHEM': "CHEMISTRY                        ",
    'CHIN': "CHINESE                          ",
    'CHST': "CHILDHOOD STUDIES                ",
    'CIAR': "CLEVELAND INSTITUTE OF ART       ",
    'CLBY': "CELL BIOLOGY                     ",
    'CLIN': "CLINICAL CURRICULUM              ",
    'CLMI': "CLINICAL MED AND INTERNSHIPS     ",
    'CLSC': "CLASSICS                         ",
    'CMED': "CLINICAL RESEARCH - CCLCM        ",
    'CMPL': "COMPARATIVE LITERATURE           ",
    'CMPS': "COMPUTING/INFORMATION SCIENCE    ",
    'COGS': "COGNITIVE SCIENCE                ",
    'COLS': "GRADUATE SUMMER RESEARCH         ",
    'COOP': "COOPERATIVE EDUCATION            ",
    'COSI': "COMMUNICATION SCIENCES           ",
    'CRSP': "CLINICAL RESRCH SCHOLARS PROG    ",
    'DANC': "DANCE                            ",
    'DBIO': "DEVELOPMENTAL BIOLOGY            ",
    'DENC': "DENTISTRY - CLINICAL             ",
    'DEND': "DENTISTRY - DIDACTIC             ",
    'DENF': "DENTISTRY - FACULTY              ",
    'DENT': "DENTISTRY                        ",
    'DERM': "DERMATOLOGY                      ",
    'DGMS': "GENERAL MEDICAL SCIENCES         ",
    'EBME': "BIOMEDICAL ENGINEERING           ",
    'ECES': "COMPUTER ENGR AND SCIENCE        ",
    'ECHE': "CHEMICAL ENGINEERING             ",
    'ECIV': "CIVIL ENGINEERING                ",
    'ECLE': "EARLY CLINICAL EXPERIENCE        ",
    'ECMP': "COMPUTER ENGINEERING             ",
    'ECON': "ECONOMICS                        ",
    'EDJC': "EDUCATION - JOHN CARROLL UNIV    ",
    'EDMP': "EXECUTIVE DOCTOR OF MANAGEMENT   ",
    'EDUC': "EDUCATION                        ",
    'EEAP': "ELEC ENGR & APPLIED PHYSICS      ",
    'EECS': "ELECTRICAL ENGR & COMPUTER SCI   ",
    'EIND': "INDUSTRIAL ENGINEERING           ",
    'EMAC': "MACROMOLECULAR/POLYMER SCIENCE   ",
    'EMAE': "MECHANICAL & AEROSPACE ENGR      ",
    'EMBA': "EXECUTIVE MBA                    ",
    'EMMD': "EMER MEDICINE/INTEN CARE         ",
    'EMSE': "MATERIALS SCIENCE & ENGINEERNG   ",
    'ENDO': "ENDOCRINOLOGY                    ",
    'ENGL': "ENGLISH                          ",
    'ENGR': "ENGINEERING SCIENCE              ",
    'ENTP': "ENTREPRENEURSHIP                 ",
    'EPBI': "EPIDEMIOLOGY & BIOSTATISTICS     ",
    'EPOM': "PRACT ORIENTED ENGR MAST PROG    ",
    'EQUI': "OUT-OF-TOWN EQUIVALENCY          ",
    'ERAS': "ERASMUS                          ",
    'ESCI': "SYSTEMS CTRL & INDUSTRIAL ENGR   ",
    'ESTD': "ENVIRONMENTAL STUDIES            ",
    'ESYS': "SYSTEMS ENGINEERING              ",
    'ETHC': "BIOMEDICAL ETHICS                ",
    'ETHS': "ETHNIC STUDIES                   ",
    'EVHS': "ENVIRONMENTAL HEALTH SCIENCES    ",
    'EXAM': "EXAMINATION MASTER/PH.D          ",
    'EXCH': "INT'L EXCHANGE PROGRAM           ",
    'FAMD': "FAMILY MEDICINE                  ",
    'FGFM': "FAIRVIEW GEN HOSP-FAM MED        ",
    'FMCL': "FREE MEDICAL CLINIC OF CLEVE     ",
    'FRCH': "FRENCH                           ",
    'FSCC': "FIRST SEMINAR COMMON CURRIC      ",
    'FSCS': "FIRST SEMINAR CONT  SEMESTER     ",
    'FSNA': "FIRST SEMINAR NATURAL WORLD      ",
    'FSSO': "FIRST SEMINAR SOCIAL WORLD       ",
    'FSSY': "FIRST SEMINAR SYMBOLIC WORLD     ",
    'FSTS': "FIRST SEMINAR TRANSFER SUPPLEM   ",
    'GAST': "GASTROENTEROLOGY                 ",
    'GEMD': "GERIATRIC MEDICINE               ",
    'GENE': "GENETICS                         ",
    'GEOL': "GEOLOGY                          ",
    'GEOM': "GEOGRAPHIC MEDICINE              ",
    'GERM': "GERMAN                           ",
    'GERO': "GERONTOLOGICAL STUDIES           ",
    'GREK': "GREEK                            ",
    'GRMN': "GERMAN                           ",
    'GVHA': "GLENVILLE HEALTH ASSOCIATION     ",
    'HBRW': "HEBREW                           ",
    'HDEV': "INTERDISC PROG: HUM DEVELOPMNT   ",
    'HEMA': "HEMATOLOGY-ONCOLOGY              ",
    'HLTH': "COMMUNITY HEALTH                 ",
    'HNHC': "HOUGH NORWOOD HEALTH CENTER      ",
    'HRAM': "HURON RD HOSP AMBUL MED          ",
    'HSMC': "HEALTH SYSTEMS MANAGEMENT        ",
    'HSST': "HIST OF SCIENCE & TECHNOLOGY     ",
    'HSTY': "HISTORY                          ",
    'HUMN': "HUMANITIES                       ",
    'IBIS': "INTEGRATED BIOLOGICAL SCIENCES   ",
    'IBMS': "INTEGRATED BIOLOGICAL STUDIES    ",
    'IDHS': "INTERDISCIPLINARY HEALTH STUD    ",
    'IIME': "INST FOR INTEGR OF MGMT & ENGR   ",
    'IMMU': "IMMUNOLOGY AND INFECTIOUS DIS    ",
    'INTC': "INTENSIVE CARE                   ",
    'INTH': "INTERNATIONAL HEALTH             ",
    'INTL': "INTERNATIONAL STUDIES            ",
    'ITAL': "ITALIAN                          ",
    'JAPN': "JAPANESE                         ",
    'JDST': "JUDAIC STUDIES                   ",
    'JRAB': "JUNIOR YEAR ABROAD               ",
    'LAPP': "LAW & PUBLIC POLICY              ",
    'LATN': "LATIN                            ",
    'LAWS': "LAW                              ",
    'LCAN': "CANADIAN LAW COURSES             ",
    'LHRP': "LABOR & HUMAN RESOURCE POLICY    ",
    'LIBS': "LIBRARY SCIENCE                  ",
    'LITR': "LITERATURE                       ",
    'LLM ': "LL M  TAX PROGRAM                ",
    'LMON': "MONTREAL LAW COURSES             ",
    'MANC': "UNIVERSITY OF MANCHESTER         ",
    'MAND': "MANDEL CENTER                    ",
    'MAPH': "MATHEMATICAL PHYSICS             ",
    'MASS': "MEDICINE AND SOCIAL STRUCTURES   ",
    'MATH': "MATHEMATICS                      ",
    'MBAC': "MBA CORE                         ",
    'MBIO': "MOLECULAR BIOL & MICROBIOLOGY    ",
    'MCCT': "METRO CLEMENT CENTER             ",
    'MEDC': "MEDICINE CORE CLERKSHIP          ",
    'MEDG': "GENERAL MEDICINE                 ",
    'MEDT': "MEDICAL TECHNOLOGY               ",
    'MGMT': "MANAGEMENT                       ",
    'MHAM': "METRO HEALTH - AMBUL. MED.       ",
    'MHAP': "METRO HEALTH - AMBUL. PED.       ",
    'MHFM': "METRO HEALTH - FAM. MED.         ",
    'MIDS': "INFORMATION SYSTEMS              ",
    'MISC': "MISCELLANEOUS                    ",
    'MKMR': "MARKETING                        ",
    'MLIT': "MOD FOREIGN LIT & MOD LANG       ",
    'MMED': "MOLECULAR MEDICINE               ",
    'MPHP': "PUBLIC HEALTH                    ",
    'MSFM': "MT SINAI MED CENTER-FAM MED      ",
    'MSOD': "MANIFESTATIONS OF DISEASE        ",
    'MSPC': "MT SINAI MED CTR-PRIM CARE       ",
    'MSTP': "MED SCIENTIST TRAINING PROG      ",
    'MUAP': "APPLIED MUSIC                    ",
    'MUAR': "MUSIC, AUDIO RECORDING           ",
    'MUCP': "MUSIC COMPOSITION                ",
    'MUDE': "MUSIC, DALCROZE/EURYTHMICS       ",
    'MUED': "MUSIC EDUCATION                  ",
    'MUEN': "MUSIC, ENSEMBLES                 ",
    'MUGN': "MUSIC, GENERAL/MISC              ",
    'MUHI': "MUSIC HISTORY                    ",
    'MULI': "MUSIC LITERATURE                 ",
    'MUPD': "MUSIC, PEDAGOGY                  ",
    'MURP': "MUSIC, REPERTOIRE                ",
    'MUSC': "MUSIC                            ",
    'MUSD': "DOCTOR MUSICAL ARTS              ",
    'MUTH': "MUSIC THEORY                     ",
    'MVIR': "MOLECULAR VIROLOGY TRAIN  PRG    ",
    'NEUM': "NEUROLOGICAL MEDICINE            ",
    'NEUR': "NEUROSCIENCES                    ",
    'NEUS': "NEUROSCIENCES                    ",
    'NORG': "NOEWAGIAN SCHOOL OF MGMT         ",
    'NSCI': "NEUROSCIENCES                    ",
    'NTRN': "NUTRITION                        ",
    'NUAN': "NURSING ANESTHESIOLOGY           ",
    'NUND': "DOCTOR OF NURSING                ",
    'NUNI': "NURSING INFORMATICS              ",
    'NUNP': "NURSE PRACTITIONER               ",
    'NURS': "NURSING                          ",
    'OBGC': "OB/GYN CORE CLERKSHIP            ",
    'OPMT': "OPERATIONS MANAGEMENT            ",
    'OPRE': "OPERATIONS RESEARCH              ",
    'OPTH': "OPTHALMOLOGY                     ",
    'ORBH': "ORGANIZATIONAL BEHAVIOR          ",
    'ORTH': "ORTHOPAEDIC SURGERY              ",
    'OTHR': "OTHER                            ",
    'OTOL': "OTOLARYNGOLOGY                   ",
    'OUTC': "OUT OF TOWN CORE CLERKSHIP       ",
    'PATH': "PATHOLOGY                        ",
    'PBPG': "PATIENT BASED PROGRAM            ",
    'PCHP': "PRIMARY CARE HEALTH POLICY       ",
    'PCPC': "PRIMARY CARE HEALTH POLICY       ",
    'PEDC': "PEDIATRIC CORE CLERKSHIP         ",
    'PEDS': "PEDIATRICS                       ",
    'PGOD': "PATHOGENSIS OF DISEASE           ",
    'PHCP': "HEALTH POLICY                    ",
    'PHED': "PHYSICAL EDUCATION               ",
    'PHIL': "PHILOSOPHY                       ",
    'PHOL': "PHYSIOLOGY & BIOPHYSICS          ",
    'PHRM': "PHARMACOLOGY                     ",
    'PHYS': "PHYSICS                          ",
    'PLCY': "MANAGEMENT POLICY                ",
    'POSC': "POLITICAL SCIENCE                ",
    'PRAC': "PRACTICUM                        ",
    'PSCL': "PSYCHOLOGY                       ",
    'PSYC': "PSYCHIATRY CORE CLERKSHIP        ",
    'PSYY': "PSYCHIATRY                       ",
    'PSY7': "PSYCHIATRY AT BRECKSVILLE        ",
    'PULM': "PULMONARY MEDICINE               ",
    'QUMM': "QUANTITATIVE METHODS IN MGMT     ",
    'RADI': "RADIOLOGY                        ",
    'RASE': "RESEARCH & SPECIAL ELECTIVES     ",
    'RBAM': "RAINBOW BABIES & CHILD AMB       ",
    'RBIO': "REPRODUCTIVE BIOLOGY             ",
    'READ': "READING & LEARNING STRATEGIES    ",
    'REHA': "REHAB MED/OCCUPATIONAL HLTH      ",
    'RENL': "RENAL/NEPHROLOGY                 ",
    'RESC': "RESEARCH CURRICULUM              ",
    'RHEU': "CLINICAL RHEUMATOLOGY            ",
    'RLGN': "RELIGION                         ",
    'RSCH': "GRADUATE SUMMER RESEARCH         ",
    'RUSN': "RUSSIAN                          ",
    'SASS': "SASS                             ",
    'SLAM': "ST LUKE'S AMBULATORY MEDICINE    ",
    'SMAB': "SEMESTER IN ABSENTIA             ",
    'SOCI': "SOCIOLOGY                        ",
    'SPAN': "SPANISH                          ",
    'SPCL': "SUB-SPECIALITIES                 ",
    'SPPP': "SPPP - PROBLEMS/POLICY PROGRAM   ",
    'SPSM': "SPECIAL STUDIES IN MEDICINE      ",
    'SRAB': "SENIOR IN ABSENTIA               ",
    'SRCH': "SRCH - S W RESEARCH              ",
    'SSBT': "SSBT - SOCIOBEHAVIORAL THEORY    ",
    'SSPL': "SURGICAL SUB-SPECIALITIES        ",
    'SSWM': "SSWM - SOCIAL WORK METHODS       ",
    'STAT': "STATISTICS                       ",
    'SURC': "SURGERY CORE CLERKSHIP           ",
    'SURG': "SURGERY                          ",
    'SVAM': "ST VINCENT CHARITY-AMBUL MED     ",
    'SWBC': "SASS - SW METH ELEC B/C STREAM   ",
    'THTR': "THEATER ARTS                     ",
    'TRAN': "TRANSFUSION MEDICINE             ",
    'UCAP': "SAGES CAPSTONE EXPERIENCE        ",
    'UGSP': "UNDERGRADUATE SCHOLARS PROG      ",
    'UHFP': "UNIVERSITY HOSP FAMILY PRACT     ",
    'UNEL': "UNLISTED ELECTIVE                ",
    'UNIV': "UNIVERSITY STUDIES               ",
    'UROL': "UROLOGY                          ",
    'USFS': "UNIV SEMINARS FIRST SEMINAR      ",
    'USHC': "UNIVERSITY SUBURBAN HLTH CNTR    ",
    'USNA': "THINK ABOUT THE NATURAL WORLD    ",
    'USSO': "THINK ABOUT THE SOCIAL WORLD     ",
    'USSY': "THINK ABOUT THE SYMBOLIC WORLD   ",
    'WASH': "WASHINGTON SEMESTER              ",
    'WKAB': "WORK IN ABSENTIA                 ",
    'WLIT': "WORLD LITERATURE                 ",
    'WMST': "WOMEN'S STUDIES                  ",
    'WSTD': "WOMEN'S STUDIES                  ",
    'YES ': "PRE/COREQ(S) APPLY               ",
}
# Clean subject code data
for k, v in subject_codes.iteritems():
    subject_codes[k] = subject_codes[k].strip()
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
        return 0
    stat = course[criteria[0]]
    for key,value in criteria[1].items() :
        students += stat[key]
        total += stat[key] * value
   
    if students == 0 :
        return 0
    return total/students

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
