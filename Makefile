
usage:
	@echo 
	@echo " .: Project builder usage :. "
	@echo " dirs	- reate project folders"
	@echo " dev	- set env to development"
	@echo " prod	- set env to production"
	@echo

dirs:
	@echo "  Creating project folders..."
	@mkdir -p var/log
	@mkdir -p etc/
	@mkdir -p data
	@mkdir -p backup

dev:
	@cp backend/conf/manage.py-dist manage.py
	@cp backend/conf/wsgi.py-dist backend/wsgi.py
	@sed -i s/conf.production/conf.development/g manage.py
	@sed -i s/conf.production/conf.development/g backend/wsgi.py
	@echo " env set to development"

prod:
	@cp backend/conf/manage.py-dist manage.py
	@cp backend/conf/wsgi.py-dist backend/wsgi.py
	@sed -i s/conf.development/conf.production/g manage.py
	@sed -i s/conf.development/conf.production/g backend/wsgi.py
	@echo " env set to production"
