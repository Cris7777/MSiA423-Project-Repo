
# Soccer Player Class Prediction

<!-- toc -->
- [Configuring Environment](#configuring-environment)
- [Loading Data and Training Model](#loading-data-and-training-model)
- [Setting Database](#setting-database)
- [Running Flask APP](#running-flask-app)
- [Testing](#testing)
- [Cleaning](#cleaning)
<!-- tocstop -->

```
├── README.md                         <- You are here
│
├── config                            <- Configure yaml and flask
│   ├── logging                       <- Files of configurations for python loggers
│   ├── congig.yml                    <- Yaml file for loading data and training model
│   ├── flask_config.py               <- Flask configuration for web app
├── data                              <- Contains data used or generated
│
├── docs                              <- Default Sphinx project; see sphinx-doc.org for details.
├── figures                           <- Generate graphics and figures to be used in reporting
├── models                            <- Folder for model and model evaluation
├── notebooks
│   ├── develop                       <- Current notebooks being used in development
│   ├── deliver                       <- Notebooks shared with others
│   ├── archive                       <- Develop notebooks no longer being used
│   ├── EDA and Model Training.ipynb  <- Template notebook for analysis
├── src                               <- Source data for the project 
│   ├── sql                           <- SQL source code
│   ├── add_player.py                 <- Create a database and ingest data with prediction either locally or on RDS
│   ├── load_data.py                  <- Download data to the repository and upload data to s3 bucket, AWS credential configurations are required 
|	├── preprocess_data.py	          <- Add response to data and save new dataset
|	├── choose_features.py	          <- Select features for training
|	├── train_data.py	              <- Train model
|	├── evaluate_model.py	          <- Evaluate model with confusion matrix and misclassification rate
│
├── test                              <- Folder necessary for running model tests
│   ├── test_data_preparation.py      <- Test data acquisition, pre-process feature engineering
│   ├── test_model.py                 <- Test model fitting
├── run.py                            <- Use flask wrapper to run the model
Execute of one or more of the src scripts
├── app.py                            <- Folder necessary for running model tests
├── requirements.txt                  <- Python package dependencies 
```

Run the command
```bash
cd <Repo-Path> 
```
for following operations.

## Configuring Environment

The  `requirements.txt`  file contains the packages required to run the model code. An environment can be set up in three ways. 

#### With  `virtualenv`

```bash
pip install virtualenv
virtualenv cbest
source cbest/bin/activate
pip install -r requirements.txt
```

#### With  `conda`

```bash
conda create -n cbest python=3.7
conda activate cbest
pip install -r requirements.txt
```

#### With  `make`

```bash
 make venv
```

## Loading Data and Training Model

The dataset is originally from Kaggle, with over 10,000 players and 80 attributes from FIFA19.

### 1. Loading Data

Run the command

```bash
make load_data
```

or

```bash
python run.py load_data
```

to load data into the repository and upload data to your own S3 bucket. Data will be landed to `data/data.csv` by default.

### 2. Preprocessing Data

Run the command

```bash
make preprocess_data
```

or

```bash
python run.py preprocess_data
```

to add a responsive variable of binary class to the last column of the dataset, and save the new dataset to `data/clean_data.csv`.

### 3. Choosing Features

Run the command

```bash
make choose_feature
```

or

```bash
python run.py choose_feature
```

to create a dataset for model training. Seven features with highest correlations to the response variable are selected to build the model. Selected dataset is saved to `data/model_data.csv`.

### 4. Training Model

Run the command

```bash
make train_data
```

or

```bash
python run.py train_data
```

to build models for player data. Methods can be chosen from `logistic_regression`, `random_forest` and `decision_tree`. Empirically, `decision_tree` has the highest accuracy and `logistic_regression` has the lowest. Trained model will be saved to `models/model.pkl` for prediction.


### 5. Evaluating Model

Run the command

```bash
make evaluate_model
```

or

```bash
python run.py evaluate_model
```

to measure the accuracy of the model. Confusion matrix and misclassification rate are used to evaluate the model. Results will be saved to `models/evaluation.txt`

## Setting Database

### 1. Initializing Database

Database location is configured in `config/flask_config.py`. There are two ways to initialize the database with one initial player entry.

**Please make sure that you are on your own EC2 instance with RDS correctly configured if a RDS schema is needed from now on.**

#### With `python`

To initialize a database locally, run command line:

```bash
python run.py create_db --RDS False
```

To initialize a database on RDS, run command line:

```bash
python run.py create_db --RDS True
```

#### With `make`

To initialize a database locally, run command line:

```bash
make create_db_l
```

To initialize a database on RDS, run command line:

```bash
make create_db_r
```

At this stage, the database is initialized with one observation. However, this observation still lacks the response variable in the model building part, which will be added in the ingesting data part.

### 2. Ingesting New Data Entry with Response Variable

By ingesting a new data entry, the model will calculate the response according to input, and save response together with inputs to the database.

#### With `Python`

```bash
python run.py ingest_data --Value <Value> --Reactions <Reactions> --Composure <Composure> --Age <Age> --ShortPassing <ShortPassing> --Vision <Vision> --LongPassing <LongPassing> --RDS <RDS>
```

to with RDS equals `True` or `False` to indicate whether to ingest data into RDS table.

#### With `make`

run the command

```bash
make create_db_l
```
or
```bash
make create_db_l
```

to ingest data to local database or RDS table respectively.

## Running Flask APP


### 1. Setting Default Database

#### Local as Default

Run the command 

```bash
export SQLALCHEMY_DATABASE_URI='sqlite:///data/PredHist.db'
```

**The database path should be the same as the database path you set during initialization. To change local database path, please change the `engine_string` part in the `create_db` session in `run.py`.** 


Or, run the command line:

```bash
make set_db
```

#### RDS as Default

Run the command 

```bash
export SQLALCHEMY_DATABASE_URI="{conn_type}://{user}:{password}@{host}:{port}/{DATABASE_NAME}"
```

**Note: Please make sure again that RDS is configured correctly on your EC2 instance.**

### 2. Running the APP

Run the command 

```bash
python run.py app
```

to start the APP. The website is available on `<Instance IPv4 Public IP>:PORT` for EC2 and `<HOST>:PORT` locally. PORT and HOST can be changed if further distribution is made.

## Testing

All test files are in `test` folder. Run the command

```bash
make test
 ``` 
 
or

```bash
 py.test
 ``` 
 
 to test whether data loading and model training are correct. 
 
💡Note: when encountering the error of

```ruby
ImportError while importing test module '/home/ubuntu/MSiA423-Project-Repo/test/test_model.py'.

Hint: make sure your test modules/packages have valid Python names.

Traceback:

test/test_model.py:1: in <module>

import yaml

E ImportError: No module named yaml
```
If `make` command is used to create virtual environment, please try another method for environment setting fo finish the test.

## Cleaning

### 1. Cleaning Middle Files

**Note: Testing is not available after cleaning middle files.**

All middle files include `data/clean_data.csv`, `data/model_data.csv`, `data/xtest.csv`, and `data/ytest.csv` . Run the command

```bash
make clean
```
to delete all these files.

In addition, futile files such as `*.pyc`  are generating during the process, run the command

```bash
make clean-pyc
```

to delete this type of files.

### 2. Cleaning Virtual Environment

If the environment is created with `make`, run the command

```bash
make clean-env
```

to delete the environment.

If the environment is created with `conda`, run the command

```bash
conda env remove -n cbest
```

to remove the environment.

*This step is optional.*

*Template of website is from [https://colorlib.com/](https://colorlib.com/)*
