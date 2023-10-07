# from .Models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List,Union
from Models import *

class SessionContext:
    def __init__(self,database):
        self.database = database

    def __enter__(self):
        self.database.create_session()
        return self.database.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database.dispose_session()


class Database:
    def __init__(self):
        self.database_name = None
        self.database_port = None
        self.database_password = None
        self.database_username = None
        self.session_maker = None

        self.is_engine_start = None
        self.is_session_make = None

    def set_connect_param(self, username:str, password:str, port:str, database:str):
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
        self.database_username = username
        self.database_password = password
        self.database_port = port
        self.database_name = database

    def engine_op(self, operation):
        if operation == 'start':
            if self.is_engine_start:
                pass
            else:
                self.engine = create_engine(
                    f'postgresql://{self.database_username}:{self.database_password}@localhost:{self.database_port}/{self.database_name}')
                self.is_engine_start = True
        elif operation == 'dispose':
            if self.is_engine_start:

                self.engine.dispose()
                self.is_engine_start = False
            else:
                pass

    def create_session(self):
        if self.is_session_make:
            self.dispose_session()
        self.engine_op('start')
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
        self.is_session_make = True

    def dispose_session(self):
        self.session.close()
        self.is_session_make = False
        self.engine_op('dispose')

    def create_tables(self):
        """
        Creates all the tables in the database using the metadata defined in Base.

        :param self: The class instance.
        :return: None
        """
        self.engine_op("start")
        Base.metadata.create_all(self.engine)
        self.engine_op("dispose")

    def add_instance(self, instance, duplicate_check_keys:Union[None, List[str]] = None):
        """
        Adds a new instance to the database.

        :param instance: The instance to be added.
        :type instance: object
        :return: The ID of the added instance.
        :rtype: int
        """
        with SessionContext(self) as session:
            instance_model = type(instance)
            if duplicate_check_keys == None:
                duplicate_check_keys = instance.duplicate_check_keys
            else:
                duplicate_check_keys = duplicate_check_keys
            instance_duplicate_check_properties = {i: instance.__dict__[i] for i in duplicate_check_keys if
                                                   i in instance.__dict__}
            existed_instance = session.query(instance_model).filter_by(**instance_duplicate_check_properties).first()
            if existed_instance:
                instance_id = existed_instance.id
                print(f"Instance of {instance_model} already exists")

            else:
                if "id" in instance.__dict__:
                    instance_id = instance.id
                else:
                    existed_instances = session.query(instance_model)
                    existed_id = [i.id for i in existed_instances]
                    if not existed_id:
                        instance_id = 1
                    else:
                        existed_max_id = max(existed_id)
                        insert_middle = False
                        i = 1
                        for i in range(1,existed_max_id):
                            if i not in existed_id:
                                insert_middle = True
                                break
                        if insert_middle:
                            instance_id = i
                        else:
                            instance_id = existed_max_id+1
                instance.id = instance_id
                session.add(instance)
                session.commit()
                print(f"Instance of {instance_model} added")

        return instance_id

    def remove_instance(self, instance):
        with SessionContext(self) as session:
            instance_class = type(instance)
            instance_id = instance.id
            delete_instance = session.query(instance_class).filter_by(id=instance_id).first()
            session.delete(delete_instance)
            session.commit()

    def query(self, Model):
        """
        Returns a query object for the given SQLAlchemy model.

        :param Model: A SQLAlchemy model
        :type Model: SQLAlchemy Model

        :return: A query object for the given model
        :rtype: SQLAlchemy Query
        """
        with SessionContext(self) as session:
            result = session.query(Model)
        return result

    # def commit(self):
    #     """
    #     Commits the current session.
    #     """
    #     return self.session.commit()

    def update_instance(self, instance):
        with SessionContext(self) as session:
            instance_class = type(instance)
            instance_properties_dict = {i: j for i, j in instance.__dict__.items() if not i.startswith("_")}

            # check if there is a duplicate instance
            duplicate_instance = session.query(instance_class).filter_by(**instance_properties_dict).first()
            print(duplicate_instance)
            if duplicate_instance:
                print(f"Instance of {instance_class} don't need to be updated")

            # delete original instance
            original_instance = session.query(instance_class).filter_by(id=instance_properties_dict['id']).first()
            self.remove_instance(original_instance)

            # add new instance
            new_instance = instance_class(**instance_properties_dict)
            self.add_instance(new_instance)

    def get_sub_instance(self, instance, sub_instance_class):


        """
        Given an instance and the class of a sub-instance, return the sub-instance(s) associated with the instance.

        Args:
            instance (object): The instance to retrieve sub-instances from.
            sub_instance_class (class): The class of the sub-instances.

        Returns:
            object or list of objects: The sub-instance(s) associated with the instance.
        """
        with SessionContext(self) as session:
            sub_instance_class_string = sub_instance_class.__name__.lower()
            try:
                sub_instance_ids = instance.__dict__[sub_instance_class_string + "_id"]
            except KeyError:
                sub_instance_ids = instance.__dict__[sub_instance_class_string + "s_id"]
            if isinstance(sub_instance_ids, list):
                sub_instance = session.query(sub_instance_class).filter(
                    sub_instance_class.id.in_(sub_instance_ids)).all()
            else:
                sub_instance = session.query(sub_instance_class).filter(
                    sub_instance_class.id == sub_instance_ids).first()

        return sub_instance
