#!/usr/bin/python3

"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: {} <mysql username> <mysql password> <database name>'.format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id).order_by(City.id)
    for state, city in query.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
