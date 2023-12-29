import unittest
from Models import Experiment
from Database import Database


class TestDatabaseBasicMethod(unittest.TestCase):
    database = Database()
    database.set_connection_param('ray', 'cherish', '5432', 'HyperlandTest')

    def test_connection(self):
        self.assertEqual(self.database.database_username, "ray")
        self.assertEqual(self.database.database_password, "cherish")
        self.assertEqual(self.database.database_port, "5432")
        self.assertEqual(self.database.database_name, "HyperlandTest")

    def test_add_instance(self):
        experiment = Experiment(name='ExperimentAddTest')
        self.database.add_instance(experiment)

    def test_remove_instance(self):
        experiment_query = self.database.query(Experiment).filter_by(name="ExperimentAddTest").first()
        self.database.remove_instance(experiment_query)


class TestDatabaseUserDefineOperation(unittest.TestCase):
    database = Database()
    database.set_connection_param('ray', 'cherish', '5432', 'HyperlandTest')

    def test_query(self):
        experiment_query = self.database.query(Experiment).filter_by(name="ExperimentAddTest").first()
        self.assertEqual(experiment_query.name, "ExperimentAddTest")


if __name__ == "__main__":
    unittest.main()
