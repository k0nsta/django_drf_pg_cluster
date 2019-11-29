#!/bin/bash
set -e

cat >> ${PGDATA}/postgresql.conf <<EOF
wal_level = hot_standby
archive_mode = on
archive_command = 'cd .'
max_wal_senders = 2
wal_keep_segments = 10
hot_standby = on
EOF

echo "host replication repusr 0.0.0.0/0 md5" >> "$PGDATA/pg_hba.conf"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE USER $PG_REP_USER REPLICATION LOGIN CONNECTION LIMIT 100
ENCRYPTED PASSWORD '$PG_REP_PASSWORD';
EOSQL
