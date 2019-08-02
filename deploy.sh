# docker build
docker-compose build --no-cache web
docker-compose build --no-cache server

# 余計なイメージ削除
docker image prune -f

# サーバー再起動
docker stop mckingdom-web_server_1
docker-compose up -d server

# web再起動
docker stop mckingdom-web_web_1
docker-compose up -d web
