import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .backend.app import create_app
from models import setup_db, Course, Nanodegree



class AuticonTestCase(unittest.TestCase):
    """This class represents the auticon test case"""

    def setUp(self):
        """
        Define test variables and initialize app.
        References: 
        https://knowledge.udacity.com/questions/291567
        https://drive.google.com/file/d/17TMIrdO2YtVpMm8AMLvRwOIuDh-_E0U8/view
        """
        self.app = create_app()
        self.client = self.app.test_client 
        self.database_name = "auticon_test"
        self.database_path = "postgresql:///{}".format(self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
        # Set up base instances of Course and Nanodegree objects
        self.nanodegree = {
            "title": "Base Degree 1",
            "courses": "Base Course 1, Base Course 2"
        }
        self.db.session.add(nanodegree)

        self.course = {
            "name": "Base Course 1",
            "weeks": 6,
            "difficulty": 1,
            "nanodegree_id": 1
        }
        self.db.session.add(course)


    def tearDown(self):
        """Executed after reach test"""
        pass


    # Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/6_Final_Review/backend/test_flaskr.py
    def test_get_paginated_courses(self):
        """ Tests that courses paginate correctly """
        res = self.client().get("/courses")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))


    def test_404_sent_requesting_beyond_valid_page(self):
        """ Tests that non-existent pages cannot be requested """
        res = self.client().get("/courses?page=1000", json={"difficulty": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    def test_get_nanodegrees(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().get("/nanodegrees")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertEqual(len(data["nanodegrees"]))


    def test_get_courses(self):
        """ Tests that courses can be successfully retrieved """
        res = self.client().get("/nanodegrees/1/courses")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(data["nanodegrees"])


    def test_delete_course(self):
        """ Tests that a course can be successfully deleted """
        res = self.client().delete('/courses/1')
        data = json.loads(res.data)

        courses = Course.query.filter(Course.id == 1).one_or_none()


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_courses'])
        self.assertTrue(len(data['courses']))
        self.assertEqual(course, None)


    def test_add_new_course(self):
        """ Tests that a course can be successfully added """
        res = self.client().post("/courses", json=self.new_course)
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_422_if_course_creation_fails(self):
        """ Tests for failure when adding new courses """
        res = self.client().post("/courses", json=self.new_course)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], "course creation failed")


    def test_get_course_by_nanodegree(self):
        """ Tests that a course can be successfully retrieved by nanodegree """
        res = self.client().get('/nanodegrees/1/courses')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_courses'])
        self.assertTrue(data['current_nanodegree'])
        self.assertTrue(len(data['courses']))

    def test_404_get_course_by_nanodegree(self):
        """ Tests to see if nanodegree has no courses within """
        res = self.client().get('/nanodegrees/1/courses')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Error: nanodegree void of courses")



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
