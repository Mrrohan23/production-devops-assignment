#!/bin/bash

mkdir -p backups

docker exec postgres_db pg_dump -U appuser appdb > backups/db_backup.sql

echo "Database backup completed"
