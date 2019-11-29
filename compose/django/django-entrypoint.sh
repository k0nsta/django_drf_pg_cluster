#!/bin/sh

set -e
set -u


postgres_master_ready() {
python3 << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${PG_USER}",
        password="${PG_PASSWORD}",
        host="${PG_MASTER_HOST}",
        port="${PG_MASTER_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_master_ready; do
  >&2 echo 'Waiting for Master PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'Master PostgreSQL is available'

postgres_replica_ready() {
python3 << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${PG_USER}",
        password="${PG_PASSWORD}",
        host="${PG_REPLICA_HOST}",
        port="${PG_REPLICA_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_replica_ready; do
  >&2 echo 'Waiting for Replicat PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'Replica PostgreSQL is available'

exec "$@"
