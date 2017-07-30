
usage:
	@echo "  .: Project builder usage :. "
	@echo "  dirs           - create project folders"
	@echo "  venv           - check if venv folder exist, and if not - create fresh virtual env"
	@echo "  requirements   - install or upgrade dependencies listed in requirements.txt"
	@echo "  shebang        - change shebang line in manage.py to point vent python"
	@echo "  dev            - set env to development"
	@echo "  prod           - set env to production"
	@echo "  start          - starts django's development server"

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
	@echo "  -> creating new virtual env ..."
	@python3.6 -m venv ./venv
	@touch venv/sentinel

requirements: venv
	@echo "  -> installing project's dependencies ..."
	@venv/bin/python3.6 -m pip install -Ur requirements.txt

shebang:
	@echo "  -> change shebang line in manage.py to point venv python ..."

manage:
	@cp backend/conf/manage.py-dist manage.py

wsgi:
	@cp backend/conf/wsgi.py-dist backend/wsgi.py

dev: dirs venv requirements manage wsgi
	@sed -i s/conf.production/conf.development/g manage.py
	@sed -i s/conf.production/conf.development/g backend/wsgi.py
	@echo "  -> env set to development"

prod: dirs venv requirements manage wsgi
	@sed -i s/conf.development/conf.production/g manage.py
	@sed -i s/conf.development/conf.production/g backend/wsgi.py
	@echo "  -> env set to production"

start: venv requirements
	./manage.py runserver 0.0.0.0:8000
