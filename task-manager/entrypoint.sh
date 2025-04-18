#!/bin/bash

set -e

echo "Creando base de datos..."
python <<EOF
from src import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
    print("Base de datos y tablas creadas en /data/tasks.db")
EOF

ls -l /data

if [ "$#" -eq 0 ]; then
    exec flask run --host=0.0.0.0
else
    exec "$@"
fi