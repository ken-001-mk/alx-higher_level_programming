#!/usr/bin/env python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()


    state = session.query(State).filter(State.name == sys.argv[4]).first()


    if state is not None:
        print(state.id)
    else:
        print("Not found")