# Fondeadora Challenge

Reto Data Engineer para Fondeadora


## Set up

Levantar un docker container para la db con postgres.

```bash
sudo docker run -e POSTGRES_PASSWORD=password -p 5432:5432 --name fondepg postgres
```

Interfaz PGAdmin

```bash
sudo docker run -e PGADMIN_DEFAULT_EMAIL="jomsox@amores.com" -e PGADMIN_DEFAULT_PASSWORD="password" -p 5555:80 --name fondepgadmin dpage/pgadmin4
```
