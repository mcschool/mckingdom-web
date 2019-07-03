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