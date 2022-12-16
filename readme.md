#About task:
    Asnyc non-blocking API with tech: FastApi/SqlAlchemy/SqlLite + Docker
## Want to use this project?

Spin up the containers:

```sh
docker-compose up -d --build
```

Open your browser to [http://localhost:8080](http://localhost:8080) to view the app

Add statistic:

```sh
curl --location --request POST 'http://localhost:8080/api/v1/statistic' \
--header 'Content-Type: application/json' \
--data-raw '{"date": "2018-11-2", "views":123, "cost":32, "clicks":3456}'
```

Get statistic:

```sh
curl --location --request GET 'http://localhost:8080/api/v1/statistic?sort_type=desc'
```

Delete statistic:

```sh
curl --location --request DELETE 'http://localhost:8080/api/v1/statistic'
```

More docs in Swagger:
```sh
http://localhost:4015/docs
```