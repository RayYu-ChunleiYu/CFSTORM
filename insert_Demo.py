from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import *
from sqlalchemy.exc import IntegrityError

engine = create_engine('postgresql://ray:cherish@localhost:5432/ORMTest')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
materials_num = len(session.query(Material).all())
print(materials_num)
steel = Material(id=materials_num+1,name='Steel',detail={'yield strength':325})
concrete = Material(id=materials_num+1,name='Concret',detail={'yield strength':323333335})


try :
    session.add(concrete)
    session.commit()
except IntegrityError:
    session.rollback()
    existed_obj_properties = {i:j for i,j in concrete.__dict__.items() if not i.startswith("_")}
    print(existed_obj_properties)
    del existed_obj_properties['id']
    existed_obj = session.query(Material).filter_by(**existed_obj_properties).first()
    print(f"row exsited, the id is {existed_obj.id}")




