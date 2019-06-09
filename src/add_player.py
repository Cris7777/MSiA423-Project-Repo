from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
import sqlalchemy as sql
import logging
import pandas as pd
import os
import argparse
import pickle
from src.helpers.helpers import get_session, get_connection

logging.basicConfig(level = logging.DEBUG, format = '%(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger()

Base = declarative_base()

class Player(Base):
    
    """
    Create a data model for the database to be set up for capturing songs
    """

    __tablename__ = 'PredHist'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    Value = Column(String(100), unique=False, nullable=False)
    Reactions = Column(String(100), unique=False, nullable=False)
    Composure = Column(String(100), unique=False, nullable=False)
    Age = Column(String(100), unique=False, nullable=False)
    ShortPassing = Column(String(100), unique=False, nullable=False)
    Vision = Column(String(100), unique=False, nullable=False)
    LongPassing = Column(String(100), unique=False, nullable=False)
    Output = Column(String(100), unique=False, nullable=True)

    def __repr__(self):
        pred_repr = "<PredHist(id='%s', Value='%s', Reactions='%s', Composure='%s', Age='%s', ShortPassing='%s', Vision='%s', LongPassing='%s', Output='%s')>"
        return pred_repr % (self.id, self.Value, self.Reactions, self.Composure,
                            self.Age, self.ShortPassing, self.Vision, self.LongPassing, self.Output)

def create_db(args):

    """Creates a database with the data model given by obj:`apps.models.Track`
    Args:
        args: Argparse args - should include args.Value, args.Reactions, args.Composure, args.Age, args.ShortPassing, args.Vision, args.LongPassing 
    Returns: None
    """
    RDS = eval(args.RDS)
    if RDS is True:
        engine_string = get_connection()
    else:
        engine_string = args.enging_string

    engine = sql.create_engine(engine_string)

    Base.metadata.create_all(engine)
    logger.info('database created')

    session = get_session(engine_string=engine_string)

    player = Player(Value = args.Value, Reactions = args.Reactions, Composure = args.Composure, Age = args.Age, 
                    ShortPassing = args.ShortPassing, Vision = args.Vision, LongPassing = args.LongPassing)
    session.add(player)
    session.commit()
    logger.info("Database created with player info added, Value: %s, Reactions: %s, Composure: %s, Age: %s, ShortPassing: %s, Vision: %s, LongPassing: %s,", 
                args.Value, args.Reactions, args.Composure, args.Age, args.ShortPassing, args.Vision, args.LongPassing)
    session.close()

def add_soccer(args):

    """Seeds an existing database with additional players.
    Args:
        args: Argparse args - should include args.Value, args.Reactions, args.Composure, args.Age, args.ShortPassing, args.Vision, args.LongPassing
    Returns:None
    """
    RDS = eval(args.RDS)
    if RDS is True:
        engine_string = get_connection()
    else:
        engine_string = args.enging_string
    
    session = get_session(engine_string=engine_string)

    Value = int(args.Value)
    Reactions = int(args.Reactions)
    Composure = int(args.Composure)
    Age = int(args.Age)
    ShortPassing = int(args.ShortPassing)
    Vision = int(args.Vision)
    LongPassing = int(args.LongPassing)
    #Output = args.Output

    with open('models/model.pkl', "rb") as f:
        model = pickle.load(f)

    X = pd.DataFrame({'Reactions':[Reactions], 'Composure':[Composure], 'Vision': [Vision],
                    'ShortPassing': [ShortPassing], 'LongPassing': [LongPassing], 'Value':[Value], 'Age':[Age]})
    #print(X)
    Class = model.predict(X)
    if Class == 0:
        Output = 'Bad'
    else:
        Output = 'Good'
    #print(Class)
    player = Player(Value = args.Value, Reactions = args.Reactions, Composure = args.Composure, Age = args.Age, 
                    ShortPassing = args.ShortPassing, Vision = args.Vision, LongPassing = args.LongPassing, Output = Output)
    session.add(player)
    session.commit()
    logger.info("player added with info: Value: %s, Reactions: %s, Composure: %s, Age: %s, ShortPassing: %s, Vision: %s, LongPassing: %s, Output: %s", 
                args.Value, args.Reactions, args.Composure, args.Age, args.ShortPassing, args.Vision, args.LongPassing, Output)
    session.close()    