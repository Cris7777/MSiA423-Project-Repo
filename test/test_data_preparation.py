import yaml
import pandas as pd

with open('config/config.yml', 'r') as f:
    config = yaml.load(f)

def test_load_data():
    #df = pd.read_csv(path, header = 0)
    path = config['load_data_from_git']['load_csv']['path']
    df = pd.read_csv(path, header = 0)
    row = df.shape[0]
    col = df.shape[1]

    row_true = 17907
    col_true = 51

    assert row == row_true
    assert col == col_true

def test_generate_class():
    path = config['choose_features']['select_feature']['path']
    df_class = pd.read_csv(path, header = 0)
    response = config['preprocess_data']['generate_class']['response']
    class1 = df_class.groupby(response).count().iloc[0][0]
    class2 = df_class.groupby(response).count().iloc[1][0]
    total = class1 + class2
    percentage1 = class1/total
    percentage2 = class2/total

    assert percentage1 > 0.47
    assert percentage1 < 0.53
    assert percentage2 > 0.47
    assert percentage2 < 0.53

def test_select_feature():
    path = config['train_data']['split_data']['path']
    df_feature = pd.read_csv(path, header = 0)
    col = df_feature.shape[1]
    col_true = 8

    assert col == col_true




