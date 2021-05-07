# unittestのサンプル

起動

```bash
docker-compose build
docker-compose up -d
```

make test，make coverage，make cleanの実行

```bash
docker-compose exec mypython make test
docker-compose exec mypython make coverage
docker-compose exec mypython make clean
```

停止

```bash
docker-compose down
```

または

```bash
docker-compose down --rmi all --volumes --remove-orphans
```
