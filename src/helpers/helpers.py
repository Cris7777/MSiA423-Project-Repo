import datetime
import sqlalchemy
import yaml
from sqlalchemy.orm import sessionmaker
import logging
import os


# class Timer:
#     """Times the code within the with statement and logs the elapsed time when it closes.

#            Args:
#                function (string): Name of function being timed
#                logger (obj:`logging.logger`): Logger to have elapsed time logged to
#    """
#     def __init__(self, function, logger):
#         self.logger = logger
#         self.function = function

#     def __enter__(self):
#         self.start = datetime.datetime.now()

#         return self

#     def __exit__(self, *args):
#         self.end = datetime.datetime.now()
#         self.interval = self.end - self.start
#         self.logger.info("%s took %0.2f seconds", self.function, self.interval.total_seconds())


# def format_sql(sql, replace_sqlvar=None, replace_var=None, python=True):
#     """Formats SQL query string for Python interpretation and with variables replaced.

#     Args:
#         sql (string): String with SQL query
#         replace_sqlvar (dict, optional): If given, replaces variables of the format ${var:dict-key} with the value
#             in the dictionary corresponding to that dict-key.
#         replace_var (dict, optional): If given, replaces variables of the format {dict-key} with the value
#             in the dictionary corresponding to that dict-key.
#         python: If True, formats the query to be passed into a Python SQL querying function by replacing "%" with
#             "%%" since % is a special character in Python

#     Returns: string of SQL query with variables replaced and optionally formatted for Python

#     """
#     if replace_sqlvar is not None:
#         for var in replace_sqlvar:
#             sql = sql.replace("${var:%s}" % var, replace_sqlvar[var])

#     if replace_var is not None:
#         sql = sql.format(**replace_var)

#     if python:
#         sql = sql.replace("%", "%%")

#     return sql

def get_connection(engine_string = None):
    conn_type = "mysql+pymysql"
    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")
    host = os.environ.get("MYSQL_HOST")
    port = os.environ.get("MYSQL_PORT")
    DATABASE_NAME = 'msia423'
    engine_string = "{}://{}:{}@{}:{}/{}".\
                                format(conn_type, user, password, host, port, DATABASE_NAME)
    return engine_string

def get_session(engine = None, engine_string = None):
    """
    Args:
        engine_string: SQLAlchemy connection string in the form of:
            "{sqltype}://{username}:{password}@{host}:{port}/{database}"
    Returns:
        SQLAlchemy session
    """

    if engine is None and engine_string is None:
        return ValueError("`engine` or `engine_string` must be provided")
    #elif engine is None:
    #    engine = create_connection(engine_string=engine_string)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


