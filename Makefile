
usage:
	@echo 
	@echo " .: Project builder usage :. "
	@echo " dirs	- reate project folders"
	#@echo ...
	@echo

dirs:
	@echo "  Creating project folders..."
	@mkdir -p var/log
	@mkdir -p etc/
	@mkdir -p data
	@mkdir -p backup

