 install a database adapter 
          psycopg2 ---->, so Python can talk to PostgreSQL
          
 
 
 depends_on:
- db
db:
image: postgres:11



DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'db',
'PORT': 5432
}
}



docker-compose exec web pipenv install psycopg2-binary==2.8.3
psyconpg2 is adpatar between language and db

docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser

