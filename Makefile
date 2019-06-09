.PHONY: venv create_db_r create_db_l set_db load_data preprocess_data choose_feature train_data evaluate_model test app clean clean-pyc clean-env

#all: venv create_db load_data preprocess_data choose_feature train_data evaluate_model clean clean-env

#create and activate new virtual environment
cbest-env/bin/activate: requirements.txt
	test -d cbest-env || virtualenv cbest-env
	. cbest-env/bin/activate; pip install -r requirements.txt
	touch cbest-env/bin/activate

venv: cbest-env/bin/activate

#create local database with rds = False or rds table with rds = True
create_db_r:
	python run.py create_db --RDS True

create_db_l:
	python run.py create_db --RDS False

load_data:
	python run.py load_data

preprocess_data:
	python run.py preprocess_data

choose_feature:
	python run.py choose_feature

train_data:
	python run.py train_data

evaluate_model:
	python run.py evaluate_model

ingest_data_r:
	python run.py ingest_data --RDS True

ingest_data_l:
	python run.py ingest_data --RDS False

#clean all temporary data
clean:
	rm data/clean_data.csv
	rm data/model_data.csv
	rm data/xtest.csv
	rm data/ytest.csv

#clean environment
clean-env:
	rm -r cbest-env

#Run the Flask application
app:
	python run.py app

#unit tests
test:
	py.test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	rm -rf .pytest_cache




		