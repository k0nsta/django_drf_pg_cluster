FROM postgres:12.1-alpine

COPY ./compose/db/master-entrypoint.sh /docker-entrypoint-initdb.d/master-entrypoint.sh
RUN chmod 666 /docker-entrypoint-initdb.d/master-entrypoint.sh

