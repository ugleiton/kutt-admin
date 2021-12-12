.PHONY: secret-key
secret-key:
	docker exec kuttadmin sh -c "python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'"

.PHONY: build-base
build-base:
	docker build -t registry.gitlab.com/ugleiton/kutt-admin:base -f Dockerfile-base .

.PHONY: build
build:
	docker build -t registry.gitlab.com/ugleiton/kutt-admin:latest .
	docker-compose -f docker-compose-dev.yml up -d

.PHONY: restart
restart:
	docker-compose -f docker-compose-dev.yml restart


