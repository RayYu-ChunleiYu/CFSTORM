from .Models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List



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
        
        
    def add_instance(self,instance,duplicate_check_keys:List[str]=None):
        """
        Adds a new instance to the database.

        :param instance: The instance to be added.
        :type instance: object
        :return: The ID of the added instance.
        :rtype: int
        """
        session = self.session
        instance_model = type(instance)
        if not duplicate_check_keys:
            duplicate_check_keys = instance.duplicate_check_keys
        instance_duplicate_check_properties = {i:instance.__dict__[i] for i in duplicate_check_keys if i in instance.__dict__}
        existed_instance = session.query(instance_model).filter_by(**instance_duplicate_check_properties).first()
        if existed_instance:
            instance_id = existed_instance.id
            print(f"Instance of {instance_model} already exists")
        else:
            existed_instance_num = session.query(instance_model).count()
            instance_id = existed_instance_num+1
            instance.id = instance_id
            session.add(instance)
            session.commit()
            print(f"Instance of {instance_model} added")
    
            
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

    def commit(self):
        """
        Commits the current session.
        """
        return self.session.commit()
    
    
    def get_sub_instances(self,instance,sub_instance_class):
        
        sub_instance_class_string = sub_instance_class.__name__.lower()
        print(sub_instance_class_string)
        try:
            sub_instance_ids = instance.__dict__[sub_instance_class_string+"_id"]
        except KeyError:
            sub_instance_ids = instance.__dict__[sub_instance_class_string+"s_id"]
        if isinstance(sub_instance_ids,list):
            sub_instance = self.session.query(sub_instance_class).filter(sub_instance_class.id.in_(sub_instance_ids)).all()
        else:
            sub_instance = self.session.query(sub_instance_class).filter(sub_instance_class.id==sub_instance_ids).first()
            
        return sub_instance
        
        
        
        
        
    
        
        