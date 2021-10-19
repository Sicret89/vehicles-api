# Vehicles Rest API
You can: Add, rate, delete and view most rated cars.

Available online: https://quiet-journey-47208.herokuapp.com/docs/

API https://vpic.nhtsa.dot.gov/api/

# Endpoints:

POST /cars/
*e.g. {"make":"Volkswagen", "model":"Golf"}

  GET /cars/
  *fetch list of cars currently in db.

POST /rate/
*e.g. {"car":<car_id>, "rating":<1-5>}

  GET /popular/
  *show you top 10 cars currently in db according to the rating

DELETE /cars/{id}/
*delete car with given id

# Run project on local machine - use of docer-compose.

To run project on Docker on local machine:

1. Clone project to local machine
2. Run in a terminal.
3. docker-compose build
4. docker-compose up -d

Open your browser to http://localhost:8000/cars/ and you should see the browsable version of the API.

## TODO
1. Add and setup black and isort
```docker-compose run web black .```
```docker-compose run web isort .```
2. Tide up code and make it more readable
