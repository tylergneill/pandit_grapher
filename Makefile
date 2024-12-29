PYTHONPATH=$(shell pwd) python -m scripts.transform

extract:
	python -m scripts.extract

transform:
	python -m scripts.transform

analyze:
	python -m scripts.analyze

run:
	python flask_app.py