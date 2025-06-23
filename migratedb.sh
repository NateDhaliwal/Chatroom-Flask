#!/bin/bash

migrate_message="$1"

if [ -z "$migrate_message" ]; then
  flask db migrate
else
  flask db migrate -m "$migrate_message"
fi

flask db upgrade
