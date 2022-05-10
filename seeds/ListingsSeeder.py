from flask_seeder import Seeder
from api.models import db, ListingsModel, TagsModel, Listings_TagsModel
from api.models import Listings_CoursesModel


class ListingsSeeder(Seeder):
    """
    This is the listings seeder.  It will also create tags, which will
    affect the listing-tag table.
    """
    # run() will be called by Flask-Seeder

    def run(self):
        # ListingsSeeder Phase 1: Seed 'listings'
        listings = [
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

                'starred': True,

                'duration': 12,

                'app_open': '08/01/2021',

                'app_close': '12/31/2021',

                'app_link': 'https://www.amazon.jobs/en/jobs/1917408/software-development-engineer-aws?cmpid=POATAW401208B&ccuid=38158778542',

                'status': 'active'
            },
            {
                'client_id': 2,

                'position': 'Software Engineering Intern Summer 2022',

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

                'position': 'Facebook University - Engineering - Summer 2022',

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

                'status': 'active'
            },
            {
                'client_id': 4,

                'position': 'Software Engineering Student Team Member',

                'pos_responsibility': 'Attend weekly lectures on software ' +

                'engineering and work on a real world problem with a team.',

                'min_qualifications': 'C or better in COSC320.',
                'pref_qualifications': 'Senior standing and a passion for ' +
                'software development.',

                'additional_info': 'This course is two semesters long.',

                'duration': 14,

                'app_open': '03/26/2021',

                'app_close': '08/31/2021',

                'status': 'active'
            },
            {
                'client_id': 4,

                'position': 'SPAM asfjaslkfjlskfl',

                'status': 'rejected'
            },
            {
                'client_id': 1,

                'position': 'Software Development Engineering Intern',

                'pos_responsibility': 'Collaborate with experienced cross-' +
                'disciplinary Amazonians to conceive, design, and bring ' +
                'innovative products and services to market.',

                'pref_qualifications': 'Code',

                'status': 'inactive'
            },
            {
                'client_id': 3,

                'position': 'Software Engineering Intern',

                'status': 'pending'
            },
            {
                'client_id': 4,

                'position': 'Dr. Tu Software Engineering Project',

                'min_qualifications': 'C or better in COSC320.',

                'pref_qualifications': 'Senior standing and a passion for ' +
                'software development.',

                'additional_info': 'This course is two semesters long.',

                'duration': 14,

                'app_open': '03/26/2021',

                'app_close': '08/31/2021',

                'status': 'active'
            },
        ]
        for listing in listings:
            db.session.add(ListingsModel(**listing))
        db.session.commit()

        # ListingsSeeder Phase 2: Seed 'tags'
        tags = [
            'data structures and algorithms',
            'database',
            'web development',
            'testing/automation',
            'mobile development',
            'machine learning',
            'course'
        ]
        for tag in tags:
            db.session.add(TagsModel(tag))
        db.session.commit()

        # ListingsSeeder Phase 3: Seed 'listings_tags'
        listing_tag_pairs = [
            {
                'l_id': 1,
                't_id': 1
            },
            {
                'l_id': 1,
                't_id': 2
            },
            {
                'l_id': 1,
                't_id': 3
            },
            {
                'l_id': 2,
                't_id': 1
            },
            {
                'l_id': 2,
                't_id': 2
            },
            {
                'l_id': 2,
                't_id': 5
            },
            {
                'l_id': 3,
                't_id': 1
            },
            {
                'l_id': 3,
                't_id': 3
            },
            {
                'l_id': 3,
                't_id': 5
            },
            {
                'l_id': 4,
                't_id': 3
            },
            {
                'l_id': 4,
                't_id': 5
            },
            {
                'l_id': 4,
                't_id': 7
            },
            {
                'l_id': 6,
                't_id': 1
            },
            {
                'l_id': 6,
                't_id': 4
            },
            {
                'l_id': 7,
                't_id': 1
            },
            {
                'l_id': 8,
                't_id': 7
            },
            {
                'l_id': 8,
                't_id': 4
            },
            {
                'l_id': 8,
                't_id': 2
            }
        ]

        for listing_tag in listing_tag_pairs:
            db.session.add(Listings_TagsModel(**listing_tag))
        db.session.commit()

        listings_course_pairs = [
            {
                'l_id': 1,
                'c_id': 10
            },
            {
                'l_id': 1,
                'c_id': 17
            },
            {
                'l_id': 1,
                'c_id': 22
            },
            {
                'l_id': 3,
                'c_id': 10
            },
            {
                'l_id': 3,
                'c_id': 20
            },
            {
                'l_id': 3,
                'c_id': 22
            },
            {
                'l_id': 8,
                'c_id': 10
            },
            {
                'l_id': 8,
                'c_id': 20
            },
            {
                'l_id': 8,
                'c_id': 22
            },
            {
                'l_id': 4,
                'c_id': 5
            },
            {
                'l_id': 4,
                'c_id': 12
            },
            {
                'l_id': 4,
                'c_id': 19
            },
        ]

        for listing_course in listings_course_pairs:
            db.session.add(Listings_CoursesModel(**listing_course))

        db.session.commit()
