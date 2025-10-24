#!/usr/bin/python3
"""
Lists  State contain "a" objects
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

    states = session.query(
        State).filter(State.name.like('%a%')).order_by(State.id).all()

    for row in states:
        print(f"{row.id}: {row.name}")

    session.close()
