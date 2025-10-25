#!/usr/bin/python3
"""
Delete state with name contain a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
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

    results = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
