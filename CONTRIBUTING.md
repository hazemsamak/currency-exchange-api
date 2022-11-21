# CONTRIBUTING

## How to build docker image locally
```
docker build -t sharks-api .
```

## How to run the Dockerfile locally
```
docker run -dp 5050:5050 -w /app -v "$(pwd):/app" sharks-api sh -c "flask run --host 0.0.0.0 --port=5050"
```
```
docker run -dp 5050:5050 sharks-api sh -c "flask run --host 0.0.0.0 --port=5050"
```

## How to run docker-compose
```
docker compose -p sharks-api up  --build -d
```

## How to stop docker-compose
```
docker compose -p sharks-api down
```

## How to run redis 
```
docker run -p 6379:6379 redis
```

## How to run flask app locally
```
flask run --host=0.0.0.0 --port=5050
```