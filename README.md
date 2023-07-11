# REST_API_TUTORIAL

## How To Run

First of all you need to initialize a database by running

    python3 init_db.py

This creates a database.db with 6 records.

Start the flask application

    export FLASK_APP=prog_lang_app.py

    flask run -p <port number>

You can now work with the small programming language database as follow.

This is the command to get all existing programming languages:

    curl -X GET http://127.0.0.1:5001/programming_languages

This is the command to create a new programming language:

    curl -X POST http://127.0.0.1:5001/programming_languages 
    -H 'Content-Type: application/json' 
    -d '{"name": "Java", "publication_year": 1995, "contribution": "Object-oriented programming language."}'

This is the command to update an existing programming language:

    curl -X PUT http://127.0.0.1:5001/programming_languages/Java 
    -H 'Content-Type: application/json' 
    -d '{"contribution": "The JVM"}'

This is the command to delete a programming language:

    curl -X DELETE http://127.0.0.1:5001/programming_languages/COBOL


## To be Implemented in the Future 

- create a database instead of the current dictionary
- create nice project architecture
- create front end
- create ci/cd piepline (read data from other sources and insert into the database)
- see what else we can learn when implementing rest ful API
