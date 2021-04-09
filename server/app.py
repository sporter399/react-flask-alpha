from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sql_db_instance import db

def create_app():
    print("this is createapp")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///applicants.sqlite"
    db = SQLAlchemy(app)

    return app



def setup_database(app):

     with app.app_context():

        db.create_all()
        engine = db.get_engine()
        df = pd.read_csv('cs-test.csv')
        print('this is setupdatabase')
    
        if df is not None:
            return
        else:
            df.to_sql('APPLICANTS', con=engine, index_label='id')



