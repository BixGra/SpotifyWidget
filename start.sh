echo "docker build . -t spotifywidget"

docker build . -t spotifywidget

echo "docker compose up -d --remove-orphans"

docker compose up -d --remove-orphans

echo "docker image prune -a"

#docker image prune -a