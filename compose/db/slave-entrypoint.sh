#!/bin/bash

set -e

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    echo "*:*:replication:$PG_REP_USER:$PG_REP_PASSWORD" > ~/.pgpass
    cat ~/.pgpass
    chmod 600 ~/.pgpass

    until ping -c 1 -W 1 pg_master
        do
            echo "Waiting for the master..."
            sleep 1s
        done

    until pg_basebackup -h pg_master -D ${PGDATA} -U ${PG_REP_USER} -vP -w
        do
            echo "Waiting for the master to connect..."
            sleep 1s
        done

    echo "host replication repuser 0.0.0.0/0 md5" >> "$PGDATA/pg_hba.conf"
    echo "host testdb testuser web md5" >> "$PGDATA/pg_hba.conf"

    touch ${PGDATA}/standby.signal
    cat > ${PGDATA}/postgresql.conf <<EOF
primary_conninfo = 'host=pg_master port=5432 user=$PG_REP_USER password=$PG_REP_PASSWORD'
hot_standby = on
listen_addresses='*'
wal_level = replica
EOF
    chown postgres. ${PGDATA} -R
    chmod 700 ${PGDATA} -R

fi

# sed -i 's/wal_level = hot_standby/wal_level = replica/g' ${PGDATA}/postgresql.conf
exec "$@"
