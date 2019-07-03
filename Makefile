# APIサーバー起動
run_server:
	cd server && pip install -r requirements.txt && python manage.py runserver

# データベース起動
run_db:
	docker-compose up db

# マイグレーション
migrate:
	cd server/app/db/migrates && PYTHONPATH=../../ python manage.py upgrade
migrate_down:
	cd server/app/db/migrates && PYTHONPATH=../../ python manage.py downgrade 0



# requirements.txt からモジュールをinstallする
pip_install:
	pip install -r server/requirements.txt