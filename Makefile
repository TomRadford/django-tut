include .env.local
export

up:
	python3 manage.py runserver
migrations:
	python manage.py makemigrations 
migrate:
	python3 manage.py migrate
shell:
	python3 manage.py shell