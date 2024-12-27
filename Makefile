PYTHONPATH=$(shell pwd) python -m ETL.transform

extract:
	python ETL/extract.py

transform:
	python -m ETL.transform

analyze:
	python analyze.py

run:
	python flask_app.py