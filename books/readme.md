bookstore_project. Make sure you don’t forget that
period, ., at the end of the command or else Django will create an extra directory
which we don’t need

pipenv install django==2.2.7 psycopg2-binary==2.8.4

pipenv for lock advantage the requirements.txt always install originally installed package


docker-compose exec web python manage.py startapp users
docker-compose exec web python manage.py makemigrations users

create a user in pagadmin