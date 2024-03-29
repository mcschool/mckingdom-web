# APIサーバー起動
run_server:
	cd server/app/db/migrates && PYTHONPATH=../../ python manage.py upgrade
	cd ../../../
	cd server && pip install -r requirements.txt && python manage.py runserver

# データベース起動
# ホームページ起動
run_web:
	cd client/web && npm run dev

run_db:
	docker-compose up db

# マイグレーション
migrate:
	cd server/app/db/migrates && PYTHONPATH=../../ python manage.py upgrade
migrate_down:
	cd server/app/db/migrates && PYTHONPATH=../../ python manage.py downgrade 2
migrate_prod:
	cd server/app/db/migrates && FLASK_CONFIGURATION=local_production PYTHONPATH=../../ python manage.py upgrade

# fixtureデータimport
import_data:
	cd server && python manage.py import_data

# requirements.txt からモジュールをinstallする
pip_install:
	pip install -r server/requirements.txt
