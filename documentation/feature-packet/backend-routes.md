# Backend Endpoints

## Users

- POST /users - sign up
- POST /users/token - user log in
- GET /users/user_id - get specific user
- POST /users/user_id/add-friend - add friend  -- BONUS
- DELETE /users/user_id/delete-friend - delete friend -- BONUS
- DELETE /users/user_id - delete user account
- GET /users/user_id/runs - get stats on all runs for a user

## Run

- GET /runs - get feed of all runs
- POST /runs - create run
- GET /runs/run_id - get stats on a specific run for a user

## Routes

- GET /routes/search - search for routes based 
- POST /routes - create a route
- GET /routes - get a route
- PUT /routes/route_id - update specific route
- DELETE /routes/route_id - delete specific route
