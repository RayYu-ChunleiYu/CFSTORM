from Database import Database, Source

CFST_database = Database()
CFST_database.connect('ray', 'cherish', '5432', 'HyperlandTest')

# CFST_database.create_tables()

# source_1 = Source(author='radedddddddydddddd',software='edxp')

source_2 = CFST_database.query(Source).filter_by(author="changed_author").first()
# source_2.author = "changed_author"

# source_id = CFST_database.add_instance(source_1)
source_id = CFST_database.update_instance(source_2)

print(source_id)
# steel_id = CFST_database.add_instance(Steel1)
# source_1_id = CFST_database.add_instance(source_1)

# soruce_query = CFST_database.query(Source).filter_by(author="radeddddyd").all()
# print(soruce_query)
# CFST_database.remove_instance(soruce_query[0])
# soruce_query = CFST_database.query(Source).filter_by(author="radeddddyd").all()
# print(soruce_query)
