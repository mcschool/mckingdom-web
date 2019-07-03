# APIサーバー起動
run_server:
	cd server && pip install -r requirements.txt && python manage.py runserver

# requirements.txt からモジュールをinstallする
pip_install:
	pip install -r server/requirements.txt