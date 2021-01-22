PYTHON_PATH = $(or $(path), $(shell which python3))


all:
	@echo "make cleanvenv				- Remove files created by venv"
	@echo "make devenv [path=<python_path>]	- Create & setup development virtual environment"
	@exit 0

cleanvenv:
	rm -rf venv

devenv: cleanvenv
	$(PYTHON_PATH) -m venv venv
	venv/bin/pip install --upgrade pip setuptools
	venv/bin/pip install -r requirements.txt

.PHONY: all cleanvenv devenv
