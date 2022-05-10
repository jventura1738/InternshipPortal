# Justin Ventura

'''
This module contains testing data for all tests
'''

# Python imports:
import hashlib


# For hashing passwords:
def hash(password): return hashlib.sha256(password.encode()).hexdigest()


# User information:
usersInfo = [
    {
        'username': 'jventura3',
        'email': 'jventura3@gulls.salisbury.edu',
        'password': hash('justinventura426'),
        'is_admin': True
    },
    {
        'username': 'joemomma4',
        'email': 'joemomma4@gulls.salisbury.edu',
        'password': hash('password2'),
        'is_admin': False
    },
    {
        'username': 'joejoejoe',
        'email': None,
        'password': hash('password3'),
        'is_admin': False
    }
]


# Client information:
clientsInfo = [
    {
        'client_name': 'Amazon',
        'client_addr': '601 New Jersey Ave NW Suite 420,' +
        'Washington, DC 20001',
        'client_email': 'hr@amazon.com'
    },
    {
        'client_name': 'Google Inc.',
        'client_addr': '1600 Amphitheatre Pkwy, Mountain' +
        'View, CA 94043',
        'client_email': 'sundar_pichai@google.com'
    },
    {
        'client_name': 'Facebook Inc.',
        'client_addr': '1 Hacker Way, Menlo Park, CA 94025',
        'client_email': 'zuck@facebook.com'
    }
]


# Listings information:
listingsInfo = [
    {
        'client_id': 1,

        'position': 'TEST1 Summer 2022 Software Development Engineer',

        'pos_responsibility': 'Collaborate with experienced cross-' +
        'disciplinary Amazonians to conceive, design, and bring ' +
        'innovative products and services to market.',

        'min_qualifications': 'Programming experience with at least ' +
        'one modern language such as Java, C++, or C# including ' +
        'object-oriented design.',

        'pref_qualifications': 'Experience with distributed, ' +
        'multi-tiered systems, algorithms, and relational databases.',

        'additional_info': None,

        'starred': True,

        'duration': 12,

        'app_open': '08/01/2021',

        'app_close': '12/31/2021',

        'status': 'active'
    },
    {
        'client_id': 2,

        'position': 'TEST2 Software Engineering Intern Summer 2022',

        'pos_responsibility': 'You will design, test, deploy and ' +
        'maintain software solutions as you grow and evolve during ' +
        'your internship.',

        'min_qualifications': 'Experience in Software Development ' +
        'and coding in a general purpose programming language.',

        'pref_qualifications': 'Experience with data structures ' +
        'or algorithms gathered from inside or outside of school ' +
        'or work.',

        'additional_info': '(Colorado only*) Minimum salary of ' +
        '$90,000 + benefits.',

        'duration': 12,

        'app_open': '08/01/2021',

        'app_close': '12/31/2021',

        'status': 'pending'
    },
    {
        'client_id': 3,

        'position': 'TEST3 Facebook University - Engineering - Summer 2022',

        'pos_responsibility': 'Work on a project with product team ' +
        'and receive coaching from an intern manager.',

        'min_qualifications': 'Knowledge of at least one programming' +
        ' language (ie: C/C++, JavaScript, Java, PHP, Ruby, Python, ' +
        'Lua, Objective C etc.)',

        'pref_qualifications': 'Demonstrated interest in science and' +
        ' technology.',

        'duration': 10,

        'app_open': '08/01/2021',

        'app_close': '12/31/2021',

        'status': 'inactive'
    },
]


# Listings to attempt to submit:
listingsToSubmit = [
    {
        'client_name': 'Justin Inc.',
        'client_address': '9001 Ventura Ave',
        'client_city': 'Baltimore',
        'client_state': 'MD',
        'client_zip': '21202',
        'position_title': 'TEST1 Software Engineering Intern',
        'pos_responsibility': 'Learn and code',
        'min_qualifications': 'OOP, software design',
        'pref_qualifications': 'Python',
        'additional_info': 'Be a good human',
        'duration': 12,
        'app_open': '01/01/2022',
        'app_close': '04/30/2022',
        'status': 'pending'
    },
    {
        'client_name': 'Joe Momma Inc.',
        'client_address': '69420 JM Ln',
        'client_city': 'Joeland',
        'client_state': 'CA',
        'client_zip': '92677',
        'position_title': 'TEST2 Software Engineer',
        'pos_responsibility': 'Code',
        'min_qualifications': 'Bachelors',
        'pref_qualifications': '1-3 years experience',
        'additional_info': 'Joe momma',
        'duration': 0,
        'app_open': '01/01/2022',
        'app_close': '06/01/2022',
        'status': 'active'
    },
    {
        'client_name': 'Joe Momma Inc 2.',
        'client_address': '69420 JM Ln',
        'client_city': 'Joeland',
        'client_state': 'CA',
        'client_zip': '92677',
        'position_title': 'Software Engineer',
        'pos_responsibility': 'Code',
        'min_qualifications': 'Bachelors',
        'pref_qualifications': '1-3 years experience',
        'additional_info': 'Joe momma',
        'duration': 0,
        'app_open': '01/01/2022',
        'app_close': '06/01/2022',
        'status': 'inactive'
    }
]

# Tags for test cases:
tags = [
    'Python',
    'JavaScript',
    'PostgreSQL'
]

# Courses for test cases:
courses = [
    {
        'course_num': 'COSC425',
        'course_title': 'Software Engineering I',
    },
    {
        'course_num': 'COSC426',
        'course_title': 'Software Engineering II',
    }
]

adminListingInfo = [
    {
        'client_id': 1,

        'position': 'Summer 2022 Software Development Engineer',

        'pos_responsibility': 'Collaborate with experienced cross-' +
        'disciplinary Amazonians to conceive, design, and bring ' +
        'innovative products and services to market.',

        'min_qualifications': 'Programming experience with at least ' +
        'one modern language such as Java, C++, or C# including ' +
        'object-oriented design.',

        'pref_qualifications': 'Experience with distributed, ' +
        'multi-tiered systems, algorithms, and relational databases.',

        'additional_info': None,

        'starred': False,

        'duration': 12,

        'app_open': '08/01/2021',

        'app_close': '12/31/2021',

        'status': 'active',

    },
    {
        'client_id': 1,

        'position_title': 'new Summer 2022 Software Development Engineer',

        'pos_responsibility': 'new Collaborate with experienced cross-' +
        'disciplinary Amazonians to conceive, design, and bring ' +
        'innovative products and services to market.',

        'min_qualifications': 'new Programming experience with at least ' +
        'one modern language such as Java, C++, or C# including ' +
        'object-oriented design.',

        'pref_qualifications': 'new Experience with distributed, ' +
        'multi-tiered systems, algorithms, and relational databases.',

        'additional_info': 'Joe momma',

        'starred': False,

        'duration': 9,

        'app_open': '06/01/2021',

        'app_close': '11/31/2021',

        'status': 'inactive',

        'app_link': 'https://www.amazon.com',

        'tags': [],

        'su_courses': [],
    }
]
