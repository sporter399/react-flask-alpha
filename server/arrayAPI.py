from models import Variables
from sql_db_instance import db
from sqlalchemy.sql import func
from flask import jsonify


def one_query():
    print('this is onequery')
    
    income_var = (db.session.query(Variables).filter(Variables.age >= 58))
    returned = [variable.name for variable in income_var]
    print(returned)

