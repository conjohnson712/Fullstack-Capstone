import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)

  return app

APP = create_app()

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
#db_drop_and_create_all()

# ROUTES
""" Function that sets request allowances """
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", 
                        "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods", 
                        "GET,PUT,POST,DELETE,OPTIONS")

    return response

'''
Empty route handler to test base server functionality 
Reference: https://knowledge.udacity.com/questions/313462
'''
@app.route('/')
def handler():
    return jsonify({
        "success": True
    })

""" 
Function that gets the short list of nanodegrees 
Does not require special authorization to access
"""

@app.route('/nanodegrees', methods=['GET'])
def get_nanodegrees():
    try:
        # Get drinks via query, set to variable
        nanodegrees = Nanodegree.query.all()      

        # If the length of the drink list is 0, raise 404 error
        if len(nanodegrees) == 0:        
            abort(404)

        # Return JSON object with short list of drinks and 200 status
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
@app.route('/nanodegrees-detailed', methods=['GET'])
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
@app.route("/nanodegrees", methods=['POST'])
@requires_auth('post:nanodegree')
def create_nanodegree(payload):
    # Requests the JSON body
    body = request.get_json()
    nanodegree = [nanodegree.long() for nanodegree in Nanodegree.query.all()]

    # If the body comes in empty, raise a 404 error
    if len(body) == 0:
        abort(404)

    # If the required parameters for new nanodegrees aren't present, abort
    if 'title' and 'path' not in body:
        abort(422)

    # If parameters are present, return JSON object with nanodegrees.long
    # Reference: https://knowledge.udacity.com/questions/350615
    try:
        title = body['title']
        path = json.dumps(body['path'])

        nanodegree = Nanodegree(title=title, path=path)
        nanodegree.insert()

        return jsonify({
            'success': True, 
            'nanodegrees': [nanodegree.long()]
        }), 200

    # Raise 400 error for any other caught errors
    except:
        abort(403)
        



"""
Function that updates nanodegree information.
Requires Mentor authorization or higher 
:param payload {string} 'Token Payload (jwt)
:param id {integer} 'Nanodegree Serial ID'
Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/1_Requests_Review/backend/flaskr/__init__.py
"""
@app.route('/nanodegrees/<int:id>', methods=['PATCH'])
@requires_auth('patch:nanodegrees')
def update_drinks(payload, id):
    # Request JSON body
    body = request.get_json()

    try:
        # Gather nanodegrees, filtering by id
        nanodegree = Nanodegree.query.filter(Nanodegree.id == id).one_or_none()

        # If there are no nanodegrees, raise a 404 error
        if nanodegree is None:
            abort(404)

        # If JSON body doesn't contain needed parameters, raise 404
        # if "title" and 'path' not in body:
        #     abort(404)
            
        # If title and path in body, update title and path
        if "title" in body:
            nanodegree.title = body.get("title")

        if "path" in body:
            nanodegree.path = body.get("path")

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
@app.route('/nanodegrees/<int:id>', methods=['DELETE'])
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


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({
        "success": False, 
        "error": 404, 
        "message": "Resource not found"})
    ), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400, 
        "message": "Bad request"
    }), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500

@app.errorhandler(AuthError)
def not_authorized(auth_error):
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": "Not authorized" + auth_error.error
    }), 401

# Reference: https://knowledge.udacity.com/questions/355320
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    """
    Error returned if user is not authorized 
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)