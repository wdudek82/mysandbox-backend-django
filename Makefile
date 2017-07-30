
usage:
	@echo "  .: Project builder usage :. "
	@echo "  dirs           - create project folders"
	@echo "  venv           - check if venv folder exist, and if not - create fresh virtual env"
	@echo "  shebang        - change shebang line in manage.py to point vent python"
	@echo "  dev            - set env to development"
	@echo "  prod           - set env to production"

dirs:
	@echo "  -> creating project folders ..."
	@mkdir -p assets
	@mkdir -p backup
	@mkdir -p data
	@mkdir -p env
	@mkdir -p var/log

venv: requirements.txt
	@echo "  -> deleting old virtual env"	
	@rm -rf venv
	@echo "  -> creating new virtual env with pipenv..."
	@pipenv --python python3.6 install --dev
	@touch .venv/sentinel

shebang:
	@echo "  -> change shebang line in manage.py to point .venv python ..."

manage:
	@cp project/conf/manage.py-dist manage.py

wsgi:
	@cp project/conf/wsgi.py-dist project/wsgi.py

dev: dirs venv manage wsgi
	@sed -i s/conf.production/conf.development/g manage.py
	@sed -i s/conf.production/conf.development/g project/wsgi.py
	@echo "  -> env set to development"
	@pipenv shell

prod: dirs venv manage wsgi
	@sed -i s/conf.development/conf.production/g manage.py
	@sed -i s/conf.development/conf.production/g project/wsgi.py
	@echo "  -> env set to production"
	@pipenv shell

start:
	./manage.py runserver 0.0.0.0:8000
