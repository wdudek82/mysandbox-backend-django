
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
	@sed -i s/conf.production/conf.development/g manage.py
	@sed -i s/conf.settings/conf.development/g manage.py
	@sed -i s/conf.production/conf.development/g backend/wsgi.py
	@sed -i s/conf.settings/conf.development/g backend/wsgi.py
	@echo " env set to development"

prod:
	@sed -i s/conf.development/conf.production/g manage.py
	@sed -i s/conf.settings/conf.production/g manage.py
	@sed -i s/conf.development/conf.production/g backend/wsgi.py
	@sed -i s/conf.settings/conf.production/g backend/wsgi.py
	@echo " env set to production"
