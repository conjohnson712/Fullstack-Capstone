# Full Stack Capstone API

## Auticon: Autistic Training and Placement

Serves as the Capstone and final project for the Full Stack Web Developer Nanodegree through Udacity. This project is inspired by Auticon, the company that has taken me under their wing and has been training me to become a web developer. I, like many other Autistic people, struggle to find sustainable employment due to the hardships that come from being Autistic. Auticon, both in life and in this project, serve as a liaison between Autistic learners and the tech companies that will hire them. Auticon reviews a student's skills, experience, aptitude, and eagerness to learn when making decisions on enrollment. They help students find their niche of study and give them the tools to hit the ground running. 

Auticon's system is organized in a 3-tier structure. From lowest number of permissions to highest:

1. Prospective Students
   1. Permissions:
      1. Can GET Nanodegree paths
      2. Can GET Job Coach information

2. Current Students
   1. Permissions:
      1. Can GET Nanodegree paths
      2. Can GET Nanodegree paths with individual courses listed (details)

3. Mentors
   1. Permissions: 
      1. Can GET Nanodegree paths
      2. Can GET Nanodegree path details
      4. Can POST Nanodgree paths
      5. Can PATCH Nanodegree paths
      6. Can DELETE Nanodegree paths


Prospective students can browse the list of Nanodegree paths available, but can only view the name of the Nanodegree and the estimated length to complete. Once the student enrolls and gets Current Student credentials, they can then view the individual courses and subtopics that will be covered in each part of the nanodegree. Finally, Mentors are granted the permission to Post, Patch, and Delete Nanodegree paths completely. 


## Pre-Requisites and Local Development



## API Reference


### Getting Started
#TODO     Replace all of the info below once App built, this is placeholder


### Error Handling
This API returns 4 different error types: 
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 500: Internal Server Error


### Endpoints
#### GET /categories
- General: 
  - Returns a dictionary list of categories, success value, and total number of categories.
  - Results are paginated in groups of 10, though only 6 exist currently. 
  - Sample: 'curl http://127.0.0.1:5000/categories'
```
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET /questions
- General: 
  - Returns a list of all available questions, a success value, total number of questions, list of categories, and the current category. 
  - Results are paginated in groups of 10, if that many are available. 
  - Sample: 'curl http://127.0.0.1:5000/questions'
```
 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```


#### DELETE /questions/<int:question_id>
- General: 
  - Deletes a selected question from the database permanently using its ID. 
  - Returns the ID of the deleted question, a success value, the updated list of questions, and the updated total number of questions. 
  - Sample: 'curl http://127.0.0.1:5000/questions/20 -X DELETE'
```
 "deleted": 20,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```


#### POST /questions
- General: 
  - Creates a new question using JSON parameters: question, answer, difficulty, category
  - Returns the ID of the created question, a success value, the updated questions list, and the updated number of questions
  - Sample: 'curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "What year did the United State land on the moon?", "answer": "1969", "difficulty": 2, "category": "4" }'

```
"created": 27,
  "questions": [
    { ... shortened, same response as above
    }
    "success": true,
    "total_questions": 19,
    }
```


#### POST /questions/search
- General: 
  - Uses a user-selected search term to find related questions in the list.
  - Returns a JSON object containing a success value, a paginated list of the current questions that match the search term, the total number of questions, and the current category.
  - Sample: 'curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "moon"}''

```
 "currentCategory": null,
  "questions": [
    {
      "answer": "1969",
      "category": 1,
      "difficulty": 3,
      "id": 25,
      "question": "What year did the United States land on the moon?"
    },
    {
      "answer": "1969",
      "category": 4,
      "difficulty": 2,
      "id": 27,
      "question": "What year did the United State land on the moon?"
    }
  ],
  "success": true,
  "totalQuestions": 2
}
```


#### GET /categories/<int:category_id>/questions
- General: 
  - Filters questions so they appear by category.
  - Returns a JSON object containing a paginated result of questions, a success value, the list of relevant questions, and the total number of questions. 
  - Sample: 'curl http://127.0.0.1:5000/categories/3/questions'
```
 "current_category": {
    "id": 3,
    "type": "Geography"
  },
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

#### POST /quizzes
- General: 
  - The user selects a category and a list of random questions from that category are produced to begin the game.
  - Returns a JSON object only containing a success value and a singular, random question.
  - Sample: 'curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":{"type":"Science","id":1}}''

```
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```




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