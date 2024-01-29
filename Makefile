include .env
config-user-mysql:
	mysql -e "CREATE USER $(MYSQL_USER)@$(MYSQL_HOST) IDENTIFIED BY $(MYSQL_PASSWORD);"
	mysql -e "GRANT ALL PRIVILEGES ON *.* TO $(MYSQL_USER)@$(MYSQL_HOST);"