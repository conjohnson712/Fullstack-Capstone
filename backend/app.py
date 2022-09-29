import sys
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db, Nanodegree, Course
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the APP
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  return app


APP = create_app()
# cors = CORS(APP, resources={r'/*': {'origins': '*'}})

'''
The rest of this code was made referencing my Coffee_Shop_API:
https://github.com/conjohnson712/Coffee-Shop
'''
'''
@TODO uncomment the following line to initialize the database
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this function will add one
'''
db_drop_and_create_all()


''' 
Function that paginates nanodegree results 
Reference: My Trivia API project - https://github.com/conjohnson712/Trivia_API/blob/main/backend/flaskr/__init__.py
'''
NANODEGREES_PER_PAGE = 10

def paginate_nanodegrees(request, selection):
    # Limit number of nanodegrees that APPear per page
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * NANODEGREES_PER_PAGE
    end = start + NANODEGREES_PER_PAGE  

    nanodegrees = [nanodegree.format() for nanodegree in selection]
    current_nanodegrees = nanodegrees[start:end]

    return current_nanodegrees

''' 
Function that paginates nanodegree results 
Reference: My Trivia API project - https://github.com/conjohnson712/Trivia_API/blob/main/backend/flaskr/__init__.py
'''

COURSES_PER_PAGE = 5 
def paginate_courses(request, selection):
    # Limit number of nanodegrees that APPear per page
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * COURSES_PER_PAGE
    end = start + COURSES_PER_PAGE  

    courses = [course.format() for course in selection]
    current_courses = courses[start:end]

    return current_courses


# ROUTES
""" Function that sets request allowances """
@APP.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", 
                        "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods", 
                        "GET,PUT,POST,DELETE,OPTIONS")

    return response

'''
Empty route handler to test base server functionality 
Reference: https://knowledge.udacity.com/nanodegrees/313462
'''
@APP.route('/')
def handler():
    return jsonify({
        "success": True
    })


# NANODEGREE ROUTES
""" 
Function that gets the short list of nanodegrees 
Does not require special authorization to access
"""

@APP.route('/nanodegrees', methods=['GET'])
def get_nanodegrees():
    try:
        # Get nanodegrees via query, set to variable
        selection = Nanodegree.query.all()      
        

        # Paginate the available nanodegrees
        current_nanodegrees = paginate_nanodegrees(request, selection)
        nanodegrees = Nanodegree.query.all()  

        # Create a dictionary to house nanodegrees
        nanodegrees_dict = {}
        for nanodegree in nanodegrees:
            nanodegrees_dict[nanodegree.id] = nanodegree.title

        # If the length of the nanodegree list is 0, raise 404 error
        if len(nanodegrees) == 0:        
            abort(404)

        # Return JSON object with short list of nanodegrees and 200 status
        return jsonify({
            'success': True,
            'nanodegrees': [nanodegree.short() for nanodegree in nanodegrees]
        }), 200
        
    except:
        abort(422)

        

""" 
Function that returns long list of nanodegrees. 
Requires Current Student or Mentor authorization.
:param payload {string} 'Token Payload (jwt)'

""" 
@APP.route('/nanodegrees-detailed', methods=['GET'])
@requires_auth('get:nanodegrees-detailed')
def get_nanodegree_details(payload):
    try:
        # Get nanodegrees via query
        nanodegrees = Nanodegree.query.all()

        # If length of nanodegree list is 0, raise 404 error
        if len(nanodegrees) == 0: 
            abort(404)

        # Return JSON object containing long nanodegree list and 200 status
        return jsonify({
            'success': True, 
            'nanodegrees': [nanodegree.long() for nanodegree in nanodegrees]
        }), 200

    except BaseException():
        abort(403)


""" 
Function that creates a new nanodegree entry and adds it to the list. 
Requires Mentor Authorization or higher
:param payload {string} 'Token Payload (jwt)'
"""
@APP.route('/nanodegrees', methods=['POST'])
@requires_auth('post:nanodegrees')
def create_nanodegree(payload):
    # # Requests the JSON body
    body = request.get_json()
    nanodegree = [nanodegree.long() for nanodegree in Nanodegree.query.all()]
    
    # If the body comes in empty, raise a 404 error
    if len(body) == 0:
        abort(404)

    # If the required parameters for new nanodegrees aren't present, abort
    if 'title' and 'degree_path' not in body:
        abort(422)

    # If parameters are present, return JSON object with nanodegrees.long
    # Reference: https://knowledge.udacity.com/nanodegrees/350615
    try:
        title = body['title']
        degree_path = json.dumps(body['degree_path'])

        nanodegree = Nanodegree(title=title, degree_path=degree_path)
        nanodegree.insert()

        return jsonify({
            'success': True, 
            'nanodegrees': [nanodegree.long()]
        }), 200

        # Raise 403 error for any other caught errors
    except:
        abort(403)




"""
Function that updates nanodegree information.
Requires Mentor authorization or higher 
:param payload {string} 'Token Payload (jwt)
:param id {integer} 'Nanodegree Serial ID'
Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/1_Requests_Review/backend/flaskr/__init__.py
"""
@APP.route('/nanodegrees/<int:id>', methods=['PATCH'])
@requires_auth('patch:nanodegrees')
def update_nanodegrees(payload, id):
    # Request JSON body
    body = request.get_json()

    try:
        # Gather nanodegrees, filtering by id
        nanodegree = Nanodegree.query.filter(Nanodegree.id == id).one_or_none()

        # If there are no nanodegrees, raise a 404 error
        if nanodegree is None:
            abort(404)

        # If JSON body doesn't contain needed parameters, raise 404
        # if "title" and 'degree_path' not in body:
        #     abort(404)
            
        # If title and degree_path in body, update title and degree_path
        if "title" in body:
            nanodegree.title = body.get("title")

        if "degree_path" in body:
            nanodegree.degree_path = body.get("degree_path")

        nanodegree.update()      # Update nanodegree

        # Return JSON object with long nanodegree list and 200 status
        return jsonify({
            'success': True,
            'nanodegrees': [nanodegree.long()]
        }), 200

    # Have a bad request error to catch any other errors
    except BaseException:
        abort(400)




"""
Function that deletes a specific nanodegree from the menu
Requires Mentor Authorization or higher 
:param payload {string} 'Token Payload (jwt)'
:param id {integer} 'Nanodegree serial id'
"""
@APP.route('/nanodegrees/<int:id>', methods=['DELETE'])
@requires_auth('delete:nanodegrees')
def delete_nanodegrees(payload, id):
    nanodegree = Nanodegree.query.filter(Nanodegree.id == id).one_or_none()

    if nanodegree is None:
        abort(404)

    try: 
        nanodegree.delete()

        return jsonify({
            'success': True,
            'delete': id
        }), 200

    # Raise 422 error if any other errors are caught
    except BaseException: 
        abort(422)


#
# COURSE ROUTES 
#
""" 
Function that gets the list of courses
Does not require special authorization to access
"""

@APP.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Get courses via query, set to variable
        selection = Course.query.all()      
        

        # Paginate the available courses
        current_courses = paginate_courses(request, selection)
        courses = Course.query.all()  

        # Instantiation of the Nanodegree dictionary
        nanodegrees_dict = {}
        for nanodegree in nanodegrees:
            nanodegrees_dict[nanodegree.id] = nanodegree.title

        # If the length of the course list is 0, raise 404 error
        if len(courses) == 0:        
            abort(404)

        # Return JSON object with short list of courses and 200 status
        return jsonify({
            'success': True,
            'courses': [course for course in courses]
        }), 200
        
    except:
        abort(422)

""" 
Function that creates a new course entry and adds it to the list. 
Requires Mentor Authorization or higher
:param payload {string} 'Token Payload (jwt)'
"""
@APP.route('/courses', methods=['POST'])
@requires_auth('post:courses')
def create_course(payload):
    # # Requests the JSON body
    body = request.get_json()
    course = [course for course in course.query.all()]
    
    # If the body comes in empty, raise a 404 error
    if len(body) == 0:
        abort(404)

    # If the required parameters for new courses aren't present, abort
    if 'name' and 'weeks' and 'difficulty' not in body:
        abort(422)

    # If parameters are present, return JSON object with courses.long
    # Reference: https://knowledge.udacity.com/courses/350615
    try:
        name = body['name']
        weeks = body['weeks']
        difficulty = body['difficulty']

        course = Course(name=name, weeks=weeks, difficulty=difficult)
        course.insert()

        return jsonify({
            'success': True, 
            'courses': [course]
        }), 200

        # Raise 403 error for any other caught errors
    except:
        abort(403)


"""
Function that updates course information.
Requires Mentor authorization or higher 
:param payload {string} 'Token Payload (jwt)
:param id {integer} 'course Serial ID'
Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/1_Requests_Review/backend/flaskr/__init__.py
"""
@APP.route('/courses/<int:id>', methods=['PATCH'])
@requires_auth('patch:courses')
def update_courses(payload, id):
    # Request JSON body
    body = request.get_json()

    try:
        # Gather courses, filtering by id
        course = Course.query.filter(Course.id == id).one_or_none()

        # If there are no courses, raise a 404 error
        if course is None:
            abort(404)
            
        # If name, weeks, and difficulty in body, update name, weeks, and difficulty
        if "name" in body:
            course.name = body.get("name")

        if "weeks" in body:
            course.weeks = body.get("weeks")

        if "difficulty" in body:
            course.difficulty = body.get("difficulty")

        course.update()      # Update course

        # Return JSON object with long course list and 200 status
        return jsonify({
            'success': True,
            'courses': [course]
        }), 200

    # Have a bad request error to catch any other errors
    except BaseException:
        abort(400)


"""
Function that deletes a specific course from the menu
Requires Mentor Authorization or higher 
:param payload {string} 'Token Payload (jwt)'
:param id {integer} 'course serial id'
"""
@APP.route('/courses/<int:id>', methods=['DELETE'])
@requires_auth('delete:courses')
def delete_courses(payload, id):
    course = Course.query.filter(Course.id == id).one_or_none()

    if course is None:
        abort(404)

    try: 
        course.delete()

        return jsonify({
            'success': True,
            'delete': id
        }), 200

    # Raise 422 error if any other errors are caught
    except BaseException: 
        abort(422)

#
# Error Handling
#
'''
Example error handling for unprocessable entity
'''


@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@APP.errorhandler(404)
def not_found(error):
    return (
        jsonify({
        "success": False, 
        "error": 404, 
        "message": "Resource not found"})
    ), 404

@APP.errorhandler(403)
def not_permitted(error):
    return jsonify({
        "success": False, 
        "error": 403, 
        "message": "User is recognized, but lacks permission"
    }), 403

@APP.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400, 
        "message": "Bad request"
    }), 400

@APP.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500

@APP.errorhandler(AuthError)
def not_authorized(auth_error):
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": "Not authorized" + auth_error.error
    }), 401

# Reference: https://knowledge.udacity.com/nanodegrees/355320
@APP.errorhandler(AuthError)
def handle_auth_error(ex):
    """
    Error returned if user is not authorized 
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)