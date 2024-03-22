# Build the image
build:
	docker build -t casmssm/app-celery:latest .

# Dev environment
start-dev:
	docker-compose -f dev-compose.yml up -d

stop-dev:
	docker-compose -f dev-compose.yml down -t 1


# Start
start:
	docker-compose up -d

stop:
	docker-compose down -t 1

