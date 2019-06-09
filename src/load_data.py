import pandas as pd
import yaml
import argparse
import logging
import boto3

# logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
#                         format="%(asctime)-15s %(levelname)-8s %(message)s")
# logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG, format = '%(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger()

def read_data(path = None, **kwargs):
    '''
    function to load data into repo
    path: path to raw data
    returns: None
    '''

    url = 'https://raw.githubusercontent.com/Cris7777/MSiA423_data/master/data1.csv'
    df = pd.read_csv(url, index_col=0)
    df.to_csv(path)
    logger.info('data saved to %s', path)

def upload_data(input_path = None, bucket_name = None, output_path = None, **kwargs):
    '''
    function to upload data to s3 bucket
    input_path: path where data is saved locally
    bucket_name: name of your own s3 bucket
    output_path: path where data will be saved in s3
    '''
    s3 = boto3.client('s3')
    s3.upload_file(input_path, bucket_name, output_path)
    logger.info('data uploaded to s3 bucket')

def load_csv(path = None, **kwargs):
    '''
    function to read data
    path: path where data is saved locally
    returns: a pandas dataframe
    '''
    df = pd.read_csv(path, header = 0)
    logger.info('data read from %s', path)
    return df

def run_load(args):
    with open(args.config, 'r') as f:
        config = yaml.load(f)
    
    read_data(**config['load_data']['read_data'])
    upload_data(**config['load_data']['upload_data'])
    df = load_csv(**config['load_data']['load_csv'])
    logger.info('data loaded as dataframe')
    return df





