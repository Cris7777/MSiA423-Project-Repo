.PHONY: all

all: create_db load_data preprocess_data choose_feature train_data evaluate_model

create_db:
	python run.py create_db

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