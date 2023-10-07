import unittest
from Database import Database
from Models import *

from Database import Database,Source,Specimen,Steel,Concrete,Geometry,Measurement

class TestDatabaseBasicMethod(unittest.TestCase):
    database = Database()
    database.set_connection_param('ray','cherish','5432','HyperlandTest')

    def test_connection(self):

        self.assertEqual(self.database.database_username,"ray")
        self.assertEqual(self.database.database_password,"cherish")
        self.assertEqual(self.database.database_port,"5432")
        self.assertEqual(self.database.database_name,"HyperlandTest")

    def test_add_instance(self):
        experiment = Experiment(name='ExperimentAddTest')
        self.database.add_instance(experiment)
        experiment_query = self.database.query(Experiment).filter_by(name="ExperimentAddTest").first()

    def test_remove_instance(self):
        experiment_query = self.database.query(Experiment).filter_by(name="ExperimentAddTest").first()
        self.database.remove_instance(experiment_query)


if __name__ == "__main__":
    unittest.main()


    
