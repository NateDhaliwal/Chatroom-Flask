#!/bin/bash

migrate_message="$1"

echo "Initiating db..."
flask db init

echo "Migrating db..."
if [ -z "$migrate_message" ]; then
  flask db migrate
else
  flask db migrate -m "$migrate_message"
fi

echo "Upgrading db..."
flask db upgrade
