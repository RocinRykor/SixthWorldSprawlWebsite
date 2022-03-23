if [ ! -d migrations ]; then
    FLASK_APP=rrprojects flask db init
fi

FLASK_APP=rrprojects flask db migrate
FLASK_APP=rrprojects flask db upgrade
