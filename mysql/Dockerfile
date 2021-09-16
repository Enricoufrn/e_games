FROM mysql:latest

COPY ./sql-script/ /docker-entrypoint-initdb.d/

EXPOSE 3306
CMD ["mysqld"]
