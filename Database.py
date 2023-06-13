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
        session = self.sessionmake()
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
    
        session.close()
        
        return instance_id
    
    def remove_instance(self,instance):
        
        session = self.sessionmake()
        instance_class = type(instance)
        instance_id = instance.id
        delete_instance = session.query(instance_class).filter_by(id=instance_id).first()
        session.delete(delete_instance)
        session.commit()
        session.close()
        
        
    def query(self,Model):
        """
        Returns a query object for the given SQLAlchemy model.

        :param Model: A SQLAlchemy model
        :type Model: SQLAlchemy Model

        :return: A query object for the given model
        :rtype: SQLAlchemy Query
        """
        session = self.sessionmake()
        result = session.query(Model)
        session.close()
        return result

    # def commit(self):
    #     """
    #     Commits the current session.
    #     """
    #     return self.session.commit()
    
    def update_instance(self,instance):
        new_session = self.sessionmake()
        instance_class = type(instance)
        instance_properties_dict = {i:j for i,j in instance.__dict__.items() if not i.startswith("_")}
        
        
        
        # delete original instance 
        original_instance = new_session.query(instance_class).filter_by(id=instance_properties_dict['id']).first()
        new_session.close()
        self.remove_instance(original_instance)
        
        # add new instance
        new_instance = instance_class(**instance_properties_dict)
        self.add_instance(new_instance)
        
        
    
    def get_sub_instance(self,instance,sub_instance_class):
        """
        Given an instance and the class of a sub-instance, return the sub-instance(s) associated with the instance.

        Args:
            instance (object): The instance to retrieve sub-instances from.
            sub_instance_class (class): The class of the sub-instances.

        Returns:
            object or list of objects: The sub-instance(s) associated with the instance.
        """
        new_session = self.sessionmake()
        sub_instance_class_string = sub_instance_class.__name__.lower()
        instance_id = instance.id
        try:
            sub_instance_ids = instance.__dict__[sub_instance_class_string+"_id"]
        except KeyError:
            sub_instance_ids = instance.__dict__[sub_instance_class_string+"s_id"]
        if isinstance(sub_instance_ids,list):
            sub_instance = new_session.query(sub_instance_class).filter(sub_instance_class.id.in_(sub_instance_ids)).all()
        else:
            sub_instance = new_session.query(sub_instance_class).filter(sub_instance_class.id==sub_instance_ids).first()
        new_session.close()
            
        return sub_instance
        
        
        
        
        
    
        
        