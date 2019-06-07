import traceback
from flask import render_template, request, redirect, url_for
import logging.config
from flask import Flask
from src.add_player import Player
from flask_sqlalchemy import SQLAlchemy
#from SQLAlchemy import desc
import pickle
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Configure flask app from flask_config.py
app.config.from_pyfile('../config/flask_config.py')

# Define LOGGING_CONFIG in flask_config.py - path to config file for setting
# up the logger (e.g. config/logging/local.conf)

logging.config.fileConfig(app.config["LOGGING_CONFIG"])
logger = logging.getLogger("soccer-player")
logger.debug('Test log')

# Initialize the database
db = SQLAlchemy(app)
#print(db)



@app.route('/')
def index():
    """Main view that lists players in the database.
    Create view into index page that uses data queried from Player database and
    inserts it into the msiapp/templates/index.html template.
    Returns: rendered html template
    """

    try:
        player = db.session.query(Player).order_by(Player.id.desc()).limit(1).all()#limit(app.config["MAX_ROWS_SHOW"]).all()
        logger.debug("servise page accessed")
        #return render_template('index.html', players = player)
        return render_template('services.html', players = player)
    except:
        traceback.print_exc()
        logger.warning("Not able to display players, error page returned")
        return render_template('error.html')


@app.route('/add', methods=['POST'])
def add_entry():
    """View that process a POST with new song input
    :return: redirect to index page
    """
    with open('models/model.pkl', "rb") as f:
        model = pickle.load(f)
    
    try:
        Value = int(request.form['Value'])
        Reactions = int(request.form['Reactions'])
        Composure = int(request.form['Composure'])
        Age = int(request.form['Age'])
        ShortPassing = int(request.form['ShortPassing'])
        Vision = int(request.form['Vision'])
        LongPassing = int(request.form['LongPassing'])
    except:
        logger.warning('input must be integer')
        return ('error, please go back and teturn integer')

    X = pd.DataFrame({'Reactions':[Reactions], 'Composure':[Composure], 'Vision': [Vision],
                    'ShortPassing': [ShortPassing], 'LongPassing': [LongPassing], 'Value':[Value], 'Age':[Age]})
    Class = model.predict(X)
    if Class == 0:
        Output = 'Bad'
    else:
        Output = 'Good'

    try:
        
        player1 = Player(Value = request.form['Value'], Reactions = request.form['Reactions'], Composure = request.form['Composure'],
                        Age = request.form['Age'], ShortPassing = request.form['ShortPassing'], Vision = request.form['Vision'], LongPassing = request.form['LongPassing'], Output = Output)
        db.session.add(player1)
        db.session.commit()
        logger.info("New player info added, Value: %s, Reactions: %s, Composure: %s, Age: %s, ShortPassing: %s, Vision: %s, LongPassing: %s, Class: %s", 
                    request.form['Value'], request.form['Reactions'], request.form['Composure'], request.form['Age'], request.form['ShortPassing'], request.form['Vision'], request.form['LongPassing'], Output)
        return redirect(url_for('index'))
    except:
        logger.warning("Not able to display players, error page returned")
        return render_template('error.html')

@app.route('/home', methods=['POST','GET'])
def home():
    '''
    return to home page when clicking the button
    '''

    try:
        return render_template('index.html')
    except:
        logger.warning("Not able to return to index.html")
        return render_template('error.html')

@app.route('/services', methods=['POST','GET'])
def services():
    '''
    return to services page when clicking the button
    '''

    try:
        return render_template('services.html')
    except:
        logger.warning("Not able to return to services.html")
        return render_template('error.html')

@app.route('/about', methods=['POST','GET'])
def about():
    '''
    return to about page when clicking the button
    '''

    try:
        return render_template('about.html')
    except:
        logger.warning("Not able to return to about.html")
        return render_template('error.html') 

@app.route('/contact', methods=['POST','GET'])
def contact():
    '''
    return to contact page when clicking the button
    '''

    try:
        return render_template('contact.html')
    except:
        logger.warning("Not able to return to contact.html")
        return render_template('error.html')