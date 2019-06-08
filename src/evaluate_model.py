import pandas as pd
import yaml
import argparse
import logging
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import pickle
import sys

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)

def evaluate_model(modelpath = None, xtestpath = None, ytestpath = None, **kwargs):
    with open(modelpath, "rb") as f:
        model = pickle.load(f)

    X_test = pd.read_csv(xtestpath, header = 0)
    y_test = pd.read_csv(ytestpath, header = None)

    prediction = model.predict(X_test)
    confusion = confusion_matrix(y_test, prediction)
    misclassification = round((confusion[0,1] + confusion[1,0])/sum(sum(confusion)),2)
    logger.info('misclassification rate is %s, confusion matrix is %s', misclassification, confusion)
    return misclassification, confusion

def run_evaluate(args):
    with open(args.config, 'r') as f:
        config = yaml.load(f)
    misclassification, confusion = evaluate_model(**config['evaluate_model']['evaluate_model'])

    with open(args.output, 'w') as f:
        sys.stdout = f
        print('misclassification rate is:')
        print(misclassification)
        print()
        print('confusion matrix is:')
        print(confusion)
    logger.info('model evaluation saved to %s', args.output)

