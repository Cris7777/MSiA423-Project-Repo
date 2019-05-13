from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
import sqlalchemy as sql
import logging
import pandas as pd
import os
import argparse

Base = declarative_base()

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger('create_database')

class Player(Base):

    __tablename__ = 'PredHist'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    Value = Column(String(100), unique=False, nullable=False)
    Reactions = Column(String(100), unique=False, nullable=False)
    Composure = Column(String(100), unique=False, nullable=False)
    Age = Column(String(100), unique=False, nullable=False)
    ShortPassing = Column(String(100), unique=False, nullable=False)
    Vision = Column(String(100), unique=False, nullable=False)
    LongPassing = Column(String(100), unique=False, nullable=False)
    Output = Column(String(100), unique=False, nullable=False)

    def __repr__(self):
        pred_repr = "<PredHist(id='%s', Value='%s', Reactions='%s', Composure='%s', Age='%s', ShortPassing='%s', Vision='%s', LongPassing='%s', Output='%s')>"
        return pred_repr % (self.id, self.Value, self.Reactions, self.Composure,
                            self.Age, self.ShortPassing, self.Vision, self.LongPassing, self.Output)


def engine_string(RDS = False):
    if RDS is True:
        conn_type = "mysql+pymysql"
        user = os.environ.get("MYSQL_USER")
        password = os.environ.get("MYSQL_PASSWORD")
        host = os.environ.get("MYSQL_HOST")
        port = os.environ.get("MYSQL_PORT")
        DATABASE_NAME = 'msia423'
        engine_string = "{}://{}:{}@{}:{}/{}".format(conn_type, user, password, host, port, DATABASE_NAME)
        return  engine_string
    else:
        return 'sqlite:///predhist.db'




def database(args,engine=None):
    """Creates a database with the data models inherited from `Base` (Tweet and TweetScore).

    Args:
        engine (:py:class:`sqlalchemy.engine.Engine`, default None): SQLAlchemy connection engine.
            If None, `engine_string` must be provided.
        engine_string (`str`, default None): String defining SQLAlchemy connection URI in the form of
            `dialect+driver://username:password@host:port/database`. If None, `engine` must be provided.

    Returns:
        None
    """
    if engine is None:
        RDS = eval(args.RDS)
        engine = sql.create_engine(engine_string(RDS = RDS))

    Base.metadata.create_all(engine)
    logging.info("create database")

# Session = sessionmaker(bind=engine)
# session = Session()
# pred1 = Player(Value='100', Reactions='100', Composure='100', Age='20',ShortPassing='100', Vision='100', LongPassing='100', Output='100')
# pred2 = Player(Value='90', Reactions='90', Composure='90', Age='90',ShortPassing='90', Vision='90', LongPassing='90', Output='90')
# session.add(pred1)
# session.add(pred2)
# session.commit()
# query = "SELECT * FROM PredHist"
# df = pd.read_sql(query, con=engine)
# logger.info(df)
# logger.info("shape:%s"%df.shape)
# session.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create defined tables in database")
    parser.add_argument("--RDS", default="False", help="True if want to create in RDS else None")
    args = parser.parse_args()
    database(args)