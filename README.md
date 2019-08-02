# mckingdom-web

## 開発環境
### DB初回
```
$ make run_db でDB起動した後に
DBに入り以下のテーブルを作る
migrate_version
repository_id VARCHAR(255) = mckingdom
repository_path TEXT = null
version INTEGER = 0
```

### 開発環境起動
```
$ make run_db
$ make run_server
```


### CURL
```
GET
$ curl localhost:5000/api/admin/players

POST
$ curl -X POST -H "Content-Type: application/json" -d '{"uuid": "******", "name": "+++++++"}' localhost:5000/api/game/players
PATCH
curl -X PATCH -H "Content-Type: application/json" -d '{"uuid": "******", "name": "+++++++"}' localhost:5000/api/game/players

PUT
curl -X PUT -H "Content-Type: application/json" -d '{"uuid": "******", "name": "+++++++"}' localhost:5000/api/game/players

DELETE
curl -X DELETE -H "Content-Type: application/json" -d '{"uuid": "******", "name": "+++++++"}' localhost:5000/api/game/players
```
