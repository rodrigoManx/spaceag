## Setup and running instructions

You must have docker installed
1. Download or clonde this repository
2. Enter repository main folder
3. Run in a terminal `docker-compose up`
4. Run in a terminal `docker-compose run django python3 manage.py makemigrations app`
5. Run in a terminal `docker-compose run django python3 manage.py migrate`

## Demo

You can find a live demo here https://rqsn8g2ncd.execute-api.us-west-2.amazonaws.com/dev/v1/field-worker/

You can create, delete, update and list (POST, DELETE, PATCH, GET) registers with the following endpoint

/v1/field_workers/ 

### Example
To create a new field_worker

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"first_name": "Junior", "last_name": "Smith", "function": "1"}' \
  https://rqsn8g2ncd.execute-api.us-west-2.amazonaws.com/dev/v1/field-worker/
