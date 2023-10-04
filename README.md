# Simple API
Don't know what it's gonna do yet!

So far, set up a starting point for the project using FastAPI: https://fastapi.tiangolo.com/tutorial/first-steps/

## Starting the Server
Run the following to start the server. (May need to `pipenv install` if uvicorn is not found.)
```
uvicorn main:app --reload
```
Endpoints are served at `localhost:8000`: http://127.0.0.1:8000/

Append `/docs` for the Swagger documentation: http://127.0.0.1:8000/docs

## Testing the Endpoints
The project contains a collection of requests that can be used to test the API. With the server running, run `test_main.http` to verify the requests. 