run:
	docker-compose up -d
stop:
	docker-compose stop
makemigrate:
	docker-compose run --rm app flask db migrate
migrate:
	docker-compose run --rm app flask db upgrade
downgrade:
	docker-compose run --rm app flask db downgrade