from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import *

engine = create_engine('postgresql://ray:cherish@localhost:5432/ORMTest')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()


material = Material(name='Material 1')

geo_1 = Geometry(section_type='Rectangular', section_detail={'length': 1.0, 'width': 1.0}, length=1.0)
specimen_1 = Specimen(name='Specimen 1', geometry=geo_1, material=material)
source_1 = Source(detail={"author":"ray","data":"23-01-23"})

experiment_1 = Experiment(name='Experiment 1',source = source_1,specimen = specimen_1)
experiment_2 = Experiment(name='Experiment 2',source = source_1,specimen = specimen_1)


session.add(specimen_1)

session.commit()




