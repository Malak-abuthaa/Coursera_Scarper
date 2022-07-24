import unittest

from ..coursera_scraper import CourseraScraper


class CheckCoursera(unittest.TestCase):
    def setUp(self):
        self.coursera = CourseraScraper('test_result.csv')

    def test_get_coursera_courses(self):
        max_courses_count = 24
        courses = self.coursera.scrape_courses(search_keyword='google')
        self.assertLessEqual(len(courses), max_courses_count, msg='Courses scrapped more than max count')

    def test_get_course_details(self):
        courses = self.coursera.scrape_courses(search_keyword='aws')
        self.assertEqual(courses['Name'][0], 'Modern Application Development with Python on AWS')
        self.assertEqual(courses['Url'][0], 'https://www.coursera.org/specializations/aws-python-serverless-development')
        self.assertEqual(courses['Rating'][0], 4.7)
        self.assertEqual(courses['Tags'][0], 'Amazon Web Services, Application Programming Interfaces, Cloud API, Cloud Computing, Cloud Load Balancing, Computer Architecture, Computer Networking, Computer Programming, Computer Programming Tools, Data Management, Database Design, Database Theory, Databases, Network Architecture, Network Security, NoSQL, SQL, Security Engineering, Software Engineering, Software Testing, Statistical Programming, Theoretical Computer Science')


if __name__ == '__main__':
    unittest.main()