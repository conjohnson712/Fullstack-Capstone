# Full Stack Capstone API

## Auticon: Autistic Training and Placement

Serves as the Capstone and final project for the Full Stack Web Developer Nanodegree through Udacity. This project is inspired by Auticon, the company that has taken me under their wing and has been helping train me to become a web developer. Auticon partners with Udacity to provide educational resources to their learners and employees. I, like many other Autistic people, struggle to find sustainable employment due to the hardships that come from being Autistic. Auticon, both in life and in this project, serve as a liaison between Autistic learners and the tech companies that will hire them. Auticon reviews a student's skills, experience, aptitude, and eagerness to learn when making decisions on enrollment. They help students find their niche of study and give them the tools to hit the ground running. 

For this project, I have simplified Auticon's system to be organized in a 3-tier structure. From lowest number of permissions to highest:

1. Prospective Student (Public)
   1. Permissions:
      1. Can GET Nanodegree paths (basic)

2. Auticon Representative
   1. Permissions:
      1. Can GET Nanodegree paths (basic)
      2. Can GET Nanodegree path (detailed)

3. Udacity Manager
   1. Permissions: 
      1. Can GET Nanodegree paths (basic)
      2. Can GET Nanodegree path (detailed)
      3. Can POST Nanodegree paths
      4. Can PATCH Nanodegree paths
      5. Can DELETE Nanodegree paths


Prospective students can browse the list of Nanodegree paths available, but can only view the name of the Nanodegree and the estimated length to complete. The Auticon Representative is able to access more detailed information about the Nanodegree, but is not able to influence it. Udacity Managers, however, are granted the permission to Post, Patch, and Delete Nanodegree paths. 

For the purpose of confidentiality on behalf of Udacity and Auticon,all Nanodegrees, categories, and other Udacity resources are fake and created by myself.

## Pre-Requisites and Local Development



## API Reference


### Getting Started
********************************************************************
#TODO     Replace all of the info below once App built, this is placeholder

********************************************************************S
### Error Handling
This API returns 4 different error types: 
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 500: Internal Server Error


### Endpoints
#### GET /nanodegree
// TODO

## Testing
To run tests, enter the following commands into a terminal:
```
dropdb trivia_test;
createdb trivia_test;
psql trivia_test < trivia.psql;
python test_flaskr.py;
```

or if you are on Windows:
```
drop database trivia_test;
create database trivia_test;
psql -d trivia_test -U db_owner -a -f trivia.psql;
python test_flaskr.py;
```


## Special Thanks / Credit 
Credit goes to Udacity for providing the starter code for this project, as well as the previous assignments that provided the knowledge necessary to bring this project to life. Special thanks go out to Auticon for providing me with a life-changing experience over the past year that I have worked with them. The confidence, problem-solving, and tenacity that I have gained through my time with Auticon thus far is priceless and something I will forever be grateful for.