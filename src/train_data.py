import pandas as pd
import yaml
import argparse
import logging
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)

methods = dict(logistic_regression = LogisticRegression,
               random_forest = RandomForestClassifier,
               decision_tree = DecisionTreeClassifier)

def split_data(path = None, test_size = None, target = None, **kwargs):
    '''
    function to split data to train set and test set
    path: path where data with response variable is saved
    test_size: percentage of test size
    target: response variable
    returns: a trained model among logistic regression, random forest and decision tree
    '''

    model = pd.read_csv(path)

    y = model[target]
    X = model.drop(columns = target)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size)
    logger.info('train and test splitted with test size of %s', test_size)
    return X_train, X_test, y_train, y_test

def train(X_train, y_train, method = None, **kwargs):
    assert method in methods.keys()
    logger.info('%s method fitted', method)

    if method == 'logistic_regression':
        glm = LogisticRegression()
        train_model = glm.fit(X_train,y_train)
        logger.info('logistic regression fitted')
        return train_model

    elif method == 'random_forest':
        rf = RandomForestClassifier(random_state = 42)
        train_model = rf.fit(X_train, y_train)
        logger.info('random forest fitted')
        return train_model

    elif method == 'decision_tree':
        dt = DecisionTreeClassifier(random_state = 42)
        train_model = dt.fit(X_train,y_train)
        logger.info('decision tree fitted')
        return train_model
    
def run_train(args):
    with open(args.config, 'r') as f:
        config = yaml.load(f)
    X_train, X_test, y_train, y_test = split_data(**config['train_data']['split_data'])
    train_model = train(X_train, y_train, **config['train_data']['train'])
    X_test.to_csv(args.xtestpath, index = False)
    y_test.to_csv(args.ytestpath, index = False, header = False)
    logger.info('test set saved')
    with open(args.modelpath, "wb") as f:
        pickle.dump(train_model, f)
    logger.info('model saved to %s', args.modelpath)
