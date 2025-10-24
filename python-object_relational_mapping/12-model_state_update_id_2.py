#!/usr/bin/python3
"""
Script change the name of state with id 3
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

    state_update = session.query(State).filter_by(id=2).first()
    if state_update:
        state_update.name = "New Mexico"
        session.commit()

    session.close()
