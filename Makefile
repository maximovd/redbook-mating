.PHONY: all

-include .env

SHELL=/bin/bash

.DEFAULT_GOAL := help

su_create:
	@python ./redbookmating/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '111')"

migration:
	@python ./redbookmating/manage.py migrate

