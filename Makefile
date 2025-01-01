PYTHONPATH=$(shell pwd) python -m utils.transform

extract:
	python -m utils.extract

transform:
	python -m utils.transform

analyze:
	python -m utils.analyze

run:
	python flask_app.py