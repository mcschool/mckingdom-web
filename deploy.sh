git pull

# docker build
docker-compose build --no-cache web
docker-compose build --no-cache server
docker-compose build --no-cache nginx


# サーバー再起動
docker stop mckingdom-web_server_1
docker-compose up -d server

# web再起動
docker stop mckingdom-web_web_1
docker-compose up -d web

# nginx再起動
docker stop mckingdom-web_nginx_1
docker-compose up -d nginx

# 余計なコンテナ削除
docker container prune -f

# 余計なイメージ削除
docker image prune -f
