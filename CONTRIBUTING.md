# CONTRIBUTING

## How to build docker image locally
```
docker build -t exchange-rates-api .
```

## How to run the Dockerfile locally
```
docker run -dp 5050:5050 -w /app -v "$(pwd):/app" exchange-rates-api sh -c "flask run --host 0.0.0.0 --port=5050"
docker run -dp 5050:5050 exchange-rates-api sh -c "flask run --host 0.0.0.0 --port=5050"
```

## How to run docker-compose
docker compose -p sharks-api up  --build -d

## How to stop docker-compose
docker stop -p sharks-api down