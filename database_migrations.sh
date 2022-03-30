if [ ! -d migrations ]; then
    FLASK_APP=sixthworldsprawl flask db init
fi

echo "Flask migrate message: "
read message

FLASK_APP=sixthworldsprawl flask db migrate --message "$message"
FLASK_APP=sixthworldsprawl flask db upgrade
