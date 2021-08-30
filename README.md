## Setup and running instructions

You must have docker installed
1. Download or clonde this repository
2. Enter repository main folder
3. Run in a terminal `docker-compose up`
4. Run in a terminal `docker-compose run django python3 manage.py makemigrations app`
5. Run in a terminal `docker-compose run django python3 manage.py migrate`