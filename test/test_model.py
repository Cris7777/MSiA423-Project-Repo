import yaml
import pandas as pd
import pickle

with open('config/config.yml', 'r') as f:
    config = yaml.load(f)

def test_split_data():
    test_path = config['evaluate_model']['evaluate_model']['xtestpath']
    df_test = pd.read_csv(test_path, header = 0)
    file_path = config['train_data']['split_data']['path']
    df_origin = pd.read_csv(file_path, header = 0)

    test_row = df_test.shape[0]
    origin_row = df_origin.shape[0]
    percentage = test_row/origin_row
    true_percent = config['train_data']['split_data']['test_size']
    low = true_percent - 0.02
    high = true_percent + 0.02

    assert percentage>low
    assert percentage<high

def test_train():
    modelpath = config['evaluate_model']['evaluate_model']['modelpath']
    with open(modelpath, "rb") as f:
        model = pickle.load(f)
    X = pd.DataFrame({'Reactions':[96], 'Composure':[95], 'Vision': [82],
                    'ShortPassing': [81], 'LongPassing': [77], 'Value':[77000], 'Age':[33]})
    Class = model.predict(X)
    final = Class[0]
    assert final == 0 or final == 1

