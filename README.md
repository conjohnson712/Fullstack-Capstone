# Full Stack Capstone API

## Auticon: Training and Employment for Autistic Individuals

Serves as the Capstone and final project for the Full Stack Web Developer Nanodegree through Udacity. This project is inspired by Auticon, the company that has taken me under their wing and has been helping train me to become a web developer. Auticon partners with Udacity to provide educational resources to their learners and employees. I, like many other Autistic people, struggle to find sustainable employment due to the hardships that come from being Autistic. Auticon, both in life and in this project, serve as a liaison between Autistic learners and the tech companies that will hire them. Auticon reviews a student's skills, experience, aptitude, and eagerness to learn when making decisions on enrollment. They help students find their niche of study and give them the tools to hit the ground running. 

For this project, I have simplified Auticon's system to be organized in a 3-tier structure. From lowest number of permissions to highest:

1. Prospective Student (Public)
   1. Permissions:
      1. Can GET Nanodegree paths (basic)

2. Auticon Representative
   1. Permissions:
      1. Can GET Nanodegree paths (basic)
      2. Can GET Nanodegree path (detailed)
      3. Can GET Course lists
      4. Can PATCH Nanodegree paths
      5. Can PATCH Course lists

3. Udacity Manager
   1. Permissions: 
      1. Can GET Nanodegree paths (basic)
      2. Can GET Nanodegree path (detailed)
      3. Can GET Course lists
      4. Can PATCH Nanodegree paths
      5. Can PATCH Course lists 
      6. Can POST Nanodegree paths
      7. Can POST Courses to lists 
      8. Can DELETE Nanodegree paths
      9. Can DELETE Courses from lists


Prospective students and the public can browse the list of Nanodegree paths available, but can only view the name of the Nanodegree and the estimated length to complete. The Auticon Representative is able to access more detailed information about the Nanodegrees and Courses available, as well as edit information within them. Udacity Managers are given the same permissions as the Auticon Representative, but can also create and delete Nanodegrees and Courses. The Auticon Representative acts as the liaison between Prospective Students and the programs available to them through the Udacity Manager.

**IMPORTANT**:
**For the purpose of confidentiality on behalf of Udacity and Auticon,all Nanodegrees, Courses, names, and other objects featured in this project are fabricated by myself and are not real (that I know of)**. This explains the silly nature of the courses present, as I wanted to be sure that I created classes that would not actually exist on Udacity, to be safe. Udacity and Auticon have presented me with a wonderful opportunity and I would not wish to insult them or jeopardize my enrollment through them by accidentally sharing confidential information. 

## Pre-Requisites and Local Development
This project requires the use of Python, Node, and Pip. Follow the instructions within the README files found in the backend and frontend folders to get your device set up to run this project. 
## API Reference
** POST HEROKU LINK HERE **

### Getting Started
Follow the instructions within the backend README file to start the server. Then, you can follow the instructions in the frontend README file to get the frontend of the application running. 
### Error Handling
This API returns 6 different error types: 
- 400: Bad Request
- 403: Permission not found
- 404: Resource Not Found
- 422: Not Processable
- 500: Internal Server Error
- AuthError: Not Authorized


### Endpoints
#### GET /nanodegrees
- General: 
  - Returns a shortened dictionary list of nanodegrees and a success value.
  - Results are paginated in groups of 10
  - Sample: 'curl http://127.0.0.1:5000/nanodegrees'
```
{
    "nanodegrees": [
        {
            "id": 1,
            "path": [
                {
                    "name": "Introduction to Programming Basics"
                },
                {
                    "name": "Understanding Those Pesky Logins"
                }
            ],
            "title": "Introduction to Computer Basics"
        }
    ],
    "success": true
}
```

#### GET /nanodegrees-detailed
- General: 
  - Returns a full dictionary list of nanodegrees and a success value.
  - Results are paginated in groups of 10
  - Sample: 'curl http://127.0.0.1:5000/nanodegrees-detailed'
```
{
    "nanodegrees": [
        {
            "id": 1,
            "path": [
                {
                    "difficulty": 1,
                    "name": "Introduction to Programming Basics",
                    "weeks": 6
                },
                {
                    "difficulty": 1,
                    "name": "Understanding Those Pesky Logins",
                    "weeks": 3
                }
            ],
            "title": "Introduction to Computer Basics"
        }
    ],
    "success": true
}
```


#### POST /nanodegrees
**TODO


#### PATCH /nanodegrees/<int:nanodegree_id>
- General: Returns a full dictionary list of nanodegrees, the updated value, and a success value.
- Results are paginated in groups of 10
- Sample: 'curl http://127.0.0.1:5000/nanodegrees/1'
  - Patch body {"title": "PATCHed Adams"}

```
{
    "nanodegrees": [
        {
            "courses": "1: Introduction to Programming Basics, 2: Understanding Those Pesky Logins",
            "id": 1,
            "title": "PATCHed Adams"
        }
    ],
    "success": true
}
```

#### DELETE /nanodegrees/<int:nanodegree_id>
- General:
  - Returns the id of the deleted item and a success value
  - Sample: 'curl http://127.0.0.1:5000/nanodegrees/1'

```
{
    "delete": 1,
    "success": true
}
```

#### GET /courses
- General:
  - Returns a full dictionary list of courses and a success value
  - Results are paginated in groups of 5
  - Sample: 'curl http://127.0.0.1:5000/courses'

```
{
    "courses": {
        "difficulty": 1,
        "name": "Test Course 2",
        "nanodegree_id": 1,
        "weeks": 3
    },
    "success": true
}
```

#### POST /courses
- General:
  - Returns a full dictionary list of courses, including the new addition, the id of the created course, and a success value. 
  - Results are paginated in groups of 5.
  - Sample: 'curl http://127.0.0.1:5000/courses'

```
{
    "courses": [
        {
            "difficulty": 1,
            "id": 1,
            "name": "Where to Find the Power Button: Part 12",
            "nanodegree_id": 1,
            "weeks": 6
        },
        {
            "difficulty": 1,
            "id": 2,
            "name": "Test Course 2",
            "nanodegree_id": 1,
            "weeks": 3
        }
    ],
    "created": 2,
    "success": true
}
```

#### PATCH /courses/<int:course_id>
- General: 
  - Returns a dictionary list of available courses, the updated course, and a success value
  - Results are paginated in groups of 5
  - Sample: 'curl http://127.0.0.1:5000/courses/1'
    - Patch body {"name": "Where to Find the Power Button: Part 12"}

```
{
    "courses": [
        {
            "difficulty": 1,
            "id": 1,
            "name": "Where to Find the Power Button: Part 12",
            "nanodegree_id": 1,
            "weeks": 6
        }
    ],
    "success": true
}
```


#### DELETE /courses/<int:course_id>
- General: 
  - Returns the id of the deleted course and a success value
  - Sample: 'curl 127.0.0.1:5000/courses/1'

```
{
    "delete": 1,
    "success": true
}
```


## Special Thanks / Credit 
Credit goes to Udacity for providing the starter code for this project, as well as the previous assignments that provided the knowledge necessary to bring this project to life. Special thanks go out to Auticon for providing me with a life-changing experience over the past year that I have worked with them. The confidence, problem-solving, and tenacity that I have gained through my time with Auticon thus far is priceless and something I will forever be grateful for.