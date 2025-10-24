#!/usr/bin/python3
"""
Delete state with name contain a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_del = session.query(
        State).filter(State.name.like('%a%')).all()

    for state in states_del:
        session.delete(state)
    session.commit()

    session.close()
