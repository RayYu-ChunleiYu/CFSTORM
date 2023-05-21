from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import *

from sqlalchemy.exc import IntegrityError

engine = create_engine('postgresql://ray:cherish@localhost:5432/ORMTest')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

material = Material(name='Material 3')


# experiment_2 = Experiment(name='Experiment 2',source = source_1,specimen = specimen_1)


session.commit()




