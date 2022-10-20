import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
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
        # Set the token variables for authorization
        Authtoken = {
            "auticon_representative":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdmMTIwbzBLVlFyMU8zWUJ3eWRjMyJ9.eyJpc3MiOiJodHRwczovL2F1dGljb24tY29uam9objcxMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMyMGNhOGZhYzEyYmIxNjg2MTJkZWU3IiwiYXVkIjoiYXV0aWNvbiIsImlhdCI6MTY2NTU5OTkwMiwiZXhwIjoxNjY1Njg2MzAyLCJhenAiOiJhVE1kVHA0N0ZsQlU0SkE5V0lXWXpPcVBhekx5bVo0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmNvdXJzZXMiLCJnZXQ6bmFub2RlZ3JlZXMiLCJnZXQ6bmFub2RlZ3JlZXMtZGV0YWlsZWQiLCJwYXRjaDpjb3Vyc2VzIiwicGF0Y2g6bmFub2RlZ3JlZXMiXX0.viJ6dDxQuZplyJLQUr13EcGuFCtL-FBDsgRPVm44OIui55yR8FzWG3BLty8HNTXgwV9DCC7fDg4rAUgWbJK9xCH-RTMCATp9XXz-ME5ZjtbtQFeLG0WMejlV3q0hLMwp4CfpjlCidWw2Ao8Tf3M8WU4dMOAKjSnkdyluL8eEpsfFY-6JDndQnYhR3FMc709gGfipnp7sO66f8LwHn6i-DsWeL7wdO1shdFxdB7bQRjxmSZETZx0kr_ME2PooVVG0zWH2Wg1vijFjUqo1Z_DIPccH52MkdKTR7A9qVxAkVfW8OZb5miI4hXmPKSGpeUQFBJxtyV0n1YJ3MhqKCmeH8Q",
            "udacity_manager":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdmMTIwbzBLVlFyMU8zWUJ3eWRjMyJ9.eyJpc3MiOiJodHRwczovL2F1dGljb24tY29uam9objcxMi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMyMGNhZjE0NWQ3NTliYjQzNThlNTMyIiwiYXVkIjoiYXV0aWNvbiIsImlhdCI6MTY2NTU5OTc2OCwiZXhwIjoxNjY1Njg2MTY4LCJhenAiOiJhVE1kVHA0N0ZsQlU0SkE5V0lXWXpPcVBhekx5bVo0SyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmNvdXJzZXMiLCJkZWxldGU6bmFub2RlZ3JlZXMiLCJnZXQ6Y291cnNlcyIsImdldDpuYW5vZGVncmVlcyIsImdldDpuYW5vZGVncmVlcy1kZXRhaWxlZCIsInBhdGNoOmNvdXJzZXMiLCJwYXRjaDpuYW5vZGVncmVlcyIsInBvc3Q6Y291cnNlcyIsInBvc3Q6bmFub2RlZ3JlZXMiXX0.H5T2ciHQNGjPpVG4qzHUwtli0BzBieZXdBqDhXUnsdsn5yQEn6EOq4_Uso-fnAovOjNgLMRxGO2iVpcZwUQuliOohc_hCSyoi33vTDQ-KSo-70p2_tLgMNysd9KK8UBHoYA1xdkH1QkYBSC8teddDTWxhcMwkhbqyk8BNQlhTTUlS85SOGD6eMOICY13Z0IhwHYecE1dTPG9qsNlf7JVjyzxN34QZAlBbAV-EEkzG0Fm_OqOUrYSqsDuaix1BQOk52aY8yEABCDjY0XLj5EsH2dOzC0OgoVCCfMsSIaaTJqP8zV7d0xUD01OIK_6M_Muf4h07khukuoglRMA-yS3Og"
        }

        self.app = create_app()
        self.client = self.app.test_client
        self.auticon_representative = Authtoken['auticon_representative']
        self.udacity_manager = Authtoken['udacity_manager']
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


    """ Success Tests """

    # Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/6_Final_Review/backend/test_flaskr.py
    def test_a_get_courses_by_auticon_rep(self):
        """ Tests that courses paginate correctly """
        res = self.client().get("/courses", headers={"Authorization": self.auticon_representative})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))

    def test_b_get_courses_by_udacity_manager(self):
        """ Tests that courses paginate correctly """
        res = self.client().get("/courses", headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))

    def test_c_get_nanodegrees_by_auticon_rep(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().get("/nanodegrees", headers={"Authorization": self.auticon_representative})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertEqual(len(data["nanodegrees"]))


    def test_d_get_nanodegrees_by_udacity_manager(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().get("/nanodegrees", headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertEqual(len(data["nanodegrees"]))

    def test_e_get_nanodegrees_detailed_by_auticon_rep(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().get("/nanodegrees-detailed", headers={"Authorization": self.auticon_representative})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertEqual(len(data["nanodegrees"]))

    def test_f_get_nanodegrees_detailed_by_udacity_manager(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().get("/nanodegrees-detailed", maheaders={"Authorization": self.udacity_nager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertEqual(len(data["nanodegrees"]))

    def test_g_patch_courses_by_auticon_rep(self):
        """ Tests that Courses can be successfully retrieved """
        res = self.client().patch("/courses/1", headers={"Authorization": self.auticon_representative}, json={"name": "Patch 1"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))

    def test_h_patch_courses_by_udacity_manager(self):
        """ Tests that Courses can be successfully retrieved """
        res = self.client().patch("/courses/1", headers={"Authorization": self.udacity_manager}, json={"name": "Patch 2"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))


    def test_I_patch_nanodegrees_by_auticon_rep(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().patch("/nanodegrees/1", headers={"Authorization": self.auticon_representative}, json={"title": "Patch 1"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertTrue(len(data["nanodegrees"]))

    def test_j_patch_nanodegrees_by_udacity_manager(self):
        """ Tests that Nanodegrees can be successfully retrieved """
        res = self.client().patch("/nanodegrees/1", headers={"Authorization": self.udacity_manager}, json={"title": "Patch 2"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertTrue(len(data["nanodegrees"]))

    def test_k_post_courses_by_udacity_manager(self):
        """ Tests that Courses can be successfully created """
        res = self.client().post("/courses", json={"name": "Post 1", "weeks": 2, "difficulty": 1, "nanodegree_id": 1}, headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["courses"])
        self.assertTrue(len(data["courses"]))
    

    def test_L_post_nanodegrees_by_udacity_manager(self):
        """ Tests that Nanodegrees can be successfully created """
        res = self.client().post("/nanodegrees", json={"title": "Post 1", "courses": "Post Course 1"}, headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["nanodegrees"])
        self.assertTrue(len(data["nanodegrees"]))
    

    def test_m_delete_course_by_udacity_managaer(self):
        """ Tests that a course can be successfully deleted """
        res = self.client().delete('/courses/1', headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        courses = Course.query.filter(Course.id == 1).one_or_none()


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_courses'])
        self.assertTrue(len(data['courses']))
        self.assertEqual(course, None)


    def test_n_delete_nanodegree_by_udacity_managaer(self):
        """ Tests that a nanodegree can be successfully deleted """
        res = self.client().delete('/nanodegree/1', headers={"Authorization": self.udacity_manager})
        data = json.loads(res.data)

        nanodegrees = Nanodegree.query.filter(Nanodegree.id == 1).one_or_none()


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_nanodegrees'])
        self.assertTrue(len(data['nanodegrees']))
        self.assertEqual(nanodegree, None)


    """ Failure Tests """

    def test_o_404_get_courses_fail(self):
        """ Test for if get/courses fails """
        res  = self.client().get("/courses")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Courses could not be found"])

    def test_p_404_get_nanodegrees_fail(self):
        """ Test for if get/nanodegrees fails """
        res  = self.client().get("/nanodegrees")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Nanodegrees could not be found"])

    def test_q_404_get_nanodegrees_detailed_fail(self):
        """ Test for if get/nanodegrees-detailed fails """
        res  = self.client().get("/nanodegrees-detailed")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Nanodegrees-detailed could not be found"])

    def test_r_403_get_nanodegrees_detailed_fail(self):
        """ Test for if get/nanodegrees-detailed fails due to missing authorization"""
        res  = self.client().get("/nanodegrees-detailed", headers={"Authorization": ""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Proper Authorization Misssing, Cannot Retrieve Request"])

    def test_s_patch_courses_422(self):
        """ Test for if course patch request fails """
        res = self.client().patch("/courses", json={"title": "Failure"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Bad Request, check that parameters match"])

    def test_t_patch_courses_403(self):
        """ Test for if course patch request fails due to missing authorization """
        res = self.client().patch("/courses", json={"title": "Failure"}, headers={"Authorization": ""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Patch Failed. Authorization Missing"])

    def test_u_patch_nanodegrees_422(self):
        """ Test for if nanodegree patch request fails """
        res = self.client().patch("/nanodegrees", json={"name": "Failure"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Bad Request, check that parameters match"])

    def test_v_patch_nanodegrees_403(self):
        """ Test for if course patch request fails due to missing authorization """
        res = self.client().patch("/nanodegrees", json={"name": "Failure"}, headers={"Authorization": ""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Patch Failed. Authorization Missing"])

    def test_w_post_courses_422(self): 
        """ Test for failure when creating a new course """ 
        res = self.client().post("/courses", json={"day_of_week": "Tuesday"})
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Bad Request, check that parameters match actual model"])

    def test_x_post_courses_403(self): 
        """ Test for failure due to missing authorization when creating a new course""" 
        res = self.client().post("/courses", headers={"Authorization": self.auticon_representative}, json={"name": "1", "weeks": 1, "difficulty": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Authorization Missing. Only Udacity Managers can perform this action"])

    def test_y_post_nanodegrees_422(self): 
        """ Test for failure when creating a new nanodegree """ 
        res = self.client().post("/nanodegrees", json={"day_of_week": "Tuesday"})
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Bad Request, check that parameters match actual model"])

    def test_z_post_nanodegrees_403(self): 
        """ Test for failure due to missing authorization when creating a new nanodegree """ 
        res = self.client().post("/nanodegrees", headers={"Authorization": self.auticon_representative}, json={"name": "1", "weeks": 1, "difficulty": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Authorization Missing. Only Udacity Managers can perform this action"])

    def test_za_delete_courses_404(self):
        """ Tests for failure when deleting a course entry that doesn't exist """
        res = self.client().delete("/courses/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Entry to be deleted does not exist"])

    def test_zb_delete_courses_403(self):
        """ Tests for failure when deleting courses due to missing permissions"""
        res = self.client().delete("/courses/1", headers={"Authorization": self.auticon_representative})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "User does not have permission to perform delete. Only Udacity Managers have this access."])

    def test_zc_delete_nanodegrees_404(self):
        """ Tests for failure when deleting a nanodegree entry that doesn't exist """
        res = self.client().delete("/nanodegrees/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "Entry to be deleted does not exist"])

    def test_zd_delete_nanodegrees_403(self):
        """ Tests for failure when deleting nanodegrees due to missing permissions"""
        res = self.client().delete("/nanodegrees/1", headers={"Authorization": self.auticon_representative})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message', "User does not have permission to perform delete. Only Udacity Managers have this access."])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
