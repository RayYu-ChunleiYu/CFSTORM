from Database import Database,ExperimentORSimulation,Source,Specimen,Steel,Concrete,Geometry,Measurement

CFST_database = Database('ray','cherish','5432','ORMTest')

CFST_database.create_tables()

source_1 = Source(author='radeddddyd',expOrsimu='exp')

# steel_id = CFST_database.add_instance(Steel1)
# source_1_id = CFST_database.add_instance(source_1)

soruce_query = CFST_database.query(Source).filter_by(author="radeddddyd").all()
print(soruce_query)
CFST_database.remove_instance(soruce_query[0])
soruce_query = CFST_database.query(Source).filter_by(author="radeddddyd").all()
print(soruce_query)