
usage:
	@echo "  .: Project builder usage :. "
	@echo "  dirs		- reate project folders"
	@echo "  ve		- check if ve folder exist, and if not - create fresh virtual env"
	@echo "  requirements	- install or upgrade dependencies listed in requirements.txt"
	@echo "  shebang		- change shebang line in manage.py to point vent python"
	@echo "  dev		- set env to development"
	@echo "  prod		- set env to production"
	@echo "  runserver	- starts django's development server"

dirs:
	@echo "  -> creating project folders ..."
	@mkdir -p assets
	@mkdir -p backup
	@mkdir -p data
	@mkdir -p env
	@mkdir -p var/log

ve: requirements.txt
	@echo "  -> deleting old virtual env"	
	@rm -rf ve	
	@echo "  -> creating new virtual env ..."
	@virtualenv -p python3.6 ve
	@touch ve/sentinel

requirements: ve
	@echo "  -> installing project's dependencies ..."
	@ve/bin/pip install -Ur requirements.txt

shebang:
	@echo "  -> change shebang line in manage.py to point ve python ..."

manage:
	@cp backend/conf/manage.py-dist manage.py

wsgi:
	@cp backend/conf/wsgi.py-dist backend/wsgi.py

dev: dirs ve requirements manage wsgi
	@sed -i s/conf.production/conf.development/g manage.py
	@sed -i s/conf.production/conf.development/g backend/wsgi.py
	@echo "  -> env set to development"

prod: dirs ve requirements manage wsgi
	@sed -i s/conf.development/conf.production/g manage.py
	@sed -i s/conf.development/conf.production/g backend/wsgi.py
	@echo "  -> env set to production"

runserver: ve requirements
	./manage.py runserver 0.0.0.0:8000
