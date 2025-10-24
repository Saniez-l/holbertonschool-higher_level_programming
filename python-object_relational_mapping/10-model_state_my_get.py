#!/usr/bin/python3
"""
Script that prints the State object with the name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == search_name).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
