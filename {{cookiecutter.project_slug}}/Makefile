SHELL:=/bin/bash

.PHONY: check
check: venv-{{cookiecutter.project_slug}}/bin/activate
	source venv-{{cookiecutter.project_slug}}/bin/activate && \
		python3 -m pytest \
		--cov={{cookiecutter.project_slug}} \
		--doctest-modules

.PHONY: clean
clean:
	rm -rf venv-{{cookiecutter.project_slug}}

.PHONY: black
black: venv-{{cookiecutter.project_slug}}/bin/activate
	source venv-{{cookiecutter.project_slug}}/bin/activate && \
	 black {{cookiecutter.project_slug}} test

.PHONY: container-check
container-check:
	podman run -v .:/app -it --rm debian:stable /bin/bash -c \
	 "cd app && ./install-prereqs.sh && make check"

.PHONY: testwatch
testwatch:
	ls {{cookiecutter.project_slug}}/*.py \
		test/*.py \
		Makefile requirements.txt \
		| entr time make check

venv-{{cookiecutter.project_slug}}/bin/activate: requirements.txt
	rm -rf venv-{{cookiecutter.project_slug}}
	python3 -m venv venv-{{cookiecutter.project_slug}}
	source venv-{{cookiecutter.project_slug}}/bin/activate && \
	 pip3 install --upgrade pip
	source venv-{{cookiecutter.project_slug}}/bin/activate && \
	 pip3 install -r requirements.txt

