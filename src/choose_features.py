import pandas as pd
import yaml
import argparse
import logging
from src.load_data import load_csv

logging.basicConfig(level = logging.DEBUG, format = '%(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger()

def select_feature(path = None, target = None, **kwargs):
    '''
    path: input path of data
    target: name of response
    returns: a dafaframe and a list of powerful predictors
    '''
    model = pd.read_csv(path)
    predictor = model.corr().abs().unstack()[target].sort_values(ascending = False)[:8]
    predictor = list(predictor.index)
    logger.info('variables of most correlations to response are %s', predictor)
    return model, predictor

def run_choose(args):
    with open(args.config, 'r') as f:
        config = yaml.load(f)
    
    model, predictor = select_feature(**config['choose_features']['select_feature'])
    logger.info('dataframe for model created')

    model_data = model[predictor]
    model_data.to_csv(args.output, index = False)
    logger.info('data for model saved to %s', args.output)
