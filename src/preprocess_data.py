import pandas as pd
import yaml
import argparse
import logging
import statistics
from src.load_data import load_csv

logging.basicConfig(level = logging.DEBUG, format = '%(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger()

def generate_class(df, target = None, response = None, **kwargs):
    '''
    df: data
    target: column used to generate binary response
    response: binary classes
    returns: pandas dataframe with response variable generated
    '''
    classification = []
    median = statistics.median(df[target])
    for score in df[target]:
        if score <= median:
            classification.append(0)
        else:
                classification.append(1)
    df[response] = classification
    logger.info('binary class added to dataframe with column %s', response)
    return df

def clean_data(df, drop = None, **kwargs):
    '''
    function to drop the column used to generate binary response
    '''
    model = df.drop(columns = drop)
    logger.info('column for generating response dropped')
    return model

def run_class(args):
    with open(args.config, 'r') as f:
        config = yaml.load(f)

    df = load_csv(**config['load_data']['load_csv'])
    df = generate_class(df, **config['preprocess_data']['generate_class'])
    logger.info('data preprocess completed')

    df = clean_data(df, **config['preprocess_data']['clean_data'])
    logger.info('irrelevant columns dropped from dataframe')

    df.to_csv(args.output, index = False)
    logger.info('cleaned data saved to %s', args.output)
    return df