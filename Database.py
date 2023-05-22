from .Models import ExperimentORSimulation,Source,Specimen,Steel,Concrete,Geometry,Measurement,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


class Database:
    def __init__(self,username,password,port,database):
        """
        Initializes an instance of the Database with the given parameters.
        
        :param username: The username for accessing the database.
        :type username: str
        :param password: The password for accessing the database.
        :type password: str
        :param port: The port number for the database.
        :type port: int
        :param database: The name of the database to be accessed.
        :type database: str
        """
        self.engine = create_engine(f'postgresql://{username}:{password}@localhost:{port}/{database}')
        self.sessionmake = sessionmaker(bind=self.engine)
        self.session = self.sessionmake()
        
    def create_tables(self):
        """
        Creates all the tables in the database using the metadata defined in Base.

        :param self: The class instance.
        :return: None
        """
        Base.metadata.create_all(self.engine)
        
        
    def add_instance(self,instance):
        """
        Adds a new instance to the database.

        :param instance: The instance to be added.
        :type instance: object
        :return: The ID of the added instance.
        :rtype: int
        """
        session = self.session
        instance_model = type(instance)
        
        try:
            session.add(instance)
            session.commit()
            instance_id = instance.id
        except IntegrityError:
            session.rollback()
            existed_instance_properties = {i:j for i,j in instance.__dict__.items() if not i.startswith("_")}
            del existed_instance_properties['id']
            existed_instance = session.query(instance_model).filter_by(**existed_instance_properties).first()
            instance_id = existed_instance.id
            
        return instance_id
    
    def remove_instance(self,instance):
        
        session = self.session
        session.delete(instance)
        session.commit()
        
        
    def query(self,Model):
        """
        Returns a query object for the given SQLAlchemy model.

        :param Model: A SQLAlchemy model
        :type Model: SQLAlchemy Model

        :return: A query object for the given model
        :rtype: SQLAlchemy Query
        """
        return self.session.query(Model)
        
        
    
        
        