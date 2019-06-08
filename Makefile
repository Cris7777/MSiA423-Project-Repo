.PHONY: venv create_db_r create_db_l set_db load_data preprocess_data choose_feature train_data evaluate_model test app clean clean-env

#all: venv create_db load_data preprocess_data choose_feature train_data evaluate_model clean clean-env

#create and activate new virtual environment
cloud-env/bin/activate: requirements.txt
	pip install virtualenv
	test -d cloud-env || virtualenv cloud-env
	. cloud-env/bin/activate; pip install -r requirements.txt
	touch cloud-env/bin/activate

venv: cloud-env/bin/activate

#create local database with rds = False or rds table with rds = True
create_db_r:
	. cloud-env/bin/activate; python run.py create_db --RDS True

create_db_l:
	. cloud-env/bin/activate; python run.py create_db --RDS False

load_data:
	. cloud-env/bin/activate; python run.py load_data

preprocess_data:
	. cloud-env/bin/activate; python run.py preprocess_data

choose_feature:
	. cloud-env/bin/activate; python run.py choose_feature

train_data:
	. cloud-env/bin/activate; python run.py train_data

evaluate_model:
	. cloud-env/bin/activate; python run.py evaluate_model

ingest_data_r:
	. cloud-env/bin/activate; python run.py ingest_data --RDS True

ingest_data_l:
	. cloud-env/bin/activate; python run.py ingest_data --RDS False

#clean all temporary data
clean:
	. cloud-env/bin/activate; rm data/clean_data.csv
	. cloud-env/bin/activate; rm data/model_data.csv
	. cloud-env/bin/activate; rm data/xtest.csv
	. cloud-env/bin/activate; rm data/ytest.csv

#clean environment
clean-env:
	rm -r cloud-env

#Run the Flask application
app:
	. cloud-env/bin/activate; python run.py app

#unit tests
test:
	py.test

test-env:
	sudo apt install python-pytest




		