"""Enables the command line execution of multiple modules within src/

This module combines the argparsing of each module within src/ and enables the execution of the corresponding scripts
so that all module imports can be absolute with respect to the main project directory.

To understand different arguments, run `python run.py --help`
"""
import argparse
import logging.config
from src.load_data import run_load
from src.preprocess_data import run_class
from src.choose_features import run_choose
from src.train_data import run_train
from src.evaluate_model import run_evaluate
from src.add_player import create_db, add_soccer
from app import app

logging.config.fileConfig(app.config["LOGGING_CONFIG"])
logger = logging.getLogger("run-cbest-classifier")
logger.debug('Test log')

def run_app(args):
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Run components of the model source code")
    subparsers = parser.add_subparsers()

    #subparser for creating database and ingest one observation
    create = subparsers.add_parser('create_db', description = 'create a database')
    create.add_argument('--Value', default = '85000', help = 'Value of player in pounds (K)')
    create.add_argument('--Reactions', default = '91', help = 'Reactions score of player with base of 100')
    create.add_argument('--Composure', default = '93', help = 'Composure score of player with base of 100')
    create.add_argument('--Age', default = '28', help = 'Age of player')
    create.add_argument('--ShortPassing', default = '88', help = 'ShortPassing score of player with base of 100')
    create.add_argument('--Vision', default = '89', help = 'Vision score of player with base of 100')
    create.add_argument('--LongPassing', default = '92', help = 'LongPassingtion score of player with base of 100')
    create.add_argument('--Output', default = None, help = 'Class of predicton, good or bad')
    create.add_argument('--enging_string', default = 'sqlite:///data/PredHist.db', help = 'path to save database')
    create.add_argument('--RDS', default = 'True', help = 'True to use RDS')
    create.set_defaults(func = create_db)

    #subparser for ingesting data to existed database
    ingest = subparsers.add_parser('ingest_data', description = 'ingest data to created database')
    ingest.add_argument('--Value', default = '77000', help = 'Value of player in pounds (K)')
    ingest.add_argument('--Reactions', default = '100', help = 'Reactions score of player with base of 100')
    ingest.add_argument('--Composure', default = '100', help = 'Composure score of player with base of 100')
    ingest.add_argument('--Age', default = '25', help = 'Age of player')
    ingest.add_argument('--ShortPassing', default = '100', help = 'ShortPassing score of player with base of 100')
    ingest.add_argument('--Vision', default = '100', help = 'Vision score of player with base of 100')
    ingest.add_argument('--LongPassing', default = '100', help = 'reacLongPassingtion score of player with base of 100')
    #ingest.add_argument('--Output', default = None, help = 'Class of predicton, good or bad')
    ingest.add_argument('--enging_string', default = 'sqlite:///data/PredHist.db', help = 'path to save database')
    ingest.add_argument('--RDS', default = 'True', help = 'True to use RDS')
    ingest.set_defaults(func = add_soccer)

    #subparser for loading data
    load = subparsers.add_parser('load_data', description = 'load data into dataframe')
    load.add_argument('--config', default = 'config/config.yml', help = 'path to yaml file with configurations')
    #load.add_argument('--output', default = None, help = 'path to save dataset')
    load.set_defaults(func = run_load)

    #subparser for pre-processing data
    preprocess = subparsers.add_parser('preprocess_data', description = 'add binary class to data')
    preprocess.add_argument('--config', default = 'config/config.yml', help = 'path to yaml file with configurations')
    preprocess.add_argument('--output', default = 'data/clean_data.csv', help = 'path to save dataset')
    preprocess.set_defaults(func = run_class)

    #subparser for choosing feature
    feature = subparsers.add_parser('choose_feature', description = 'choose features most related to response')
    feature.add_argument('--config', default = 'config/config.yml', help = 'path to yaml file with configurations')
    feature.add_argument('--output', default = 'data/model_data.csv', help = 'path to save dataset')
    feature.set_defaults(func = run_choose)

    #subparser for training data
    train = subparsers.add_parser('train_data', description = 'train model')
    train.add_argument('--config', default = 'config/config.yml', help = 'path to yaml file with configurations')
    train.add_argument('--xtestpath', default = 'data/xtest.csv', help = 'path to save x test')
    train.add_argument('--ytestpath', default = 'data/ytest.csv', help = 'path to save y test')
    train.add_argument('--modelpath', default = 'models/model.pkl', help = 'path to save model')
    train.set_defaults(func = run_train)

    #subparser for evaluating model
    evaluate = subparsers.add_parser('evaluate_model', description = 'evaluate model with misclassification rate and confusion matrix')
    evaluate.add_argument('--config', default = 'config/config.yml', help = 'path to yaml file with configurations')
    evaluate.add_argument('--output', default = 'models/evaluation.txt', help = 'path to save model evaluation')
    evaluate.set_defaults(func = run_evaluate)

    run = subparsers.add_parser("app", description="Run Flask app")
    #run.add_argument('--RDS', default = 'False', help = 'True to run on RDS, false to run on local')
    run.set_defaults(func = run_app)

    args = parser.parse_args()
    #print(args)
    args.func(args)

    # try:
    #     func = args.func
    # except AttributeError:
    #     parser.error("too few arguments")
    # func(args)