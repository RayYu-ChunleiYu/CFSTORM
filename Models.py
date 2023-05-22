from sqlalchemy import Column, Integer, Float, String,UniqueConstraint,Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB,ARRAY

Base = declarative_base()

class ExperimentORSimulation(Base):
    __tablename__ = 'experimentOrsimulation'
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String)
    expOrsimu = Column(String)
    specimen_id = Column(Integer)
    
    load_pattern = Column(JSONB)
    
    measurements_id = Column(ARRAY(Integer))
    
    source_id = Column(Integer)
    
    duplicate_check_keys = ['name','expOrsimu','specimen_id','load_pattern','measurements_id','source_id']
    
    
class Specimen(Base):
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String)
    expOrsimu = Column(String)
    geometry_id = Column(Integer)
    steel_id = Column(Integer)
    concrete_id = Column(Integer)
    
    duplicate_check_keys = ['name','expOrsimu','geometry_id','steel_id','concrete_id']
    
class Geometry(Base):
    __tablename__ = 'geometry'
    id = Column(Integer, primary_key=True,autoincrement=False)
    
    section_type = Column(String)
    section_width = Column(Float)
    section_height = Column(Float)
    section_diameter = Column(Float)
    length = Column(Float)
    
    duplicate_chek_keys = ['section_type','section_width','section_height','section_diameter','length']
    
    
class Steel(Base):
    __tablename__ = 'steel'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String)
    yield_strength = Column(Float)
    yield_strain = Column(Float)
    elastic_modulus = Column(Float)
    ultimate_strength = Column(Float)
    ultimate_strain = Column(Float)
    possion_ratio = Column(Float)
    
    strain = Column(ARRAY(Float))
    stress = Column(ARRAY(Float))
    
    duplicate_check_keys = ['name','yield_strength','yield_strain','elastic_modulus','ultimate_strength','ultimate_strain','possion_ratio','strain','stress']
    

class Concrete(Base):
    __tablename__ = 'concrete'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String)
    peak_strain = Column(Float)
    peak_stress = Column(Float)
    elastic_modulus = Column(Float)
    possion_ratio = Column(Float)
    
    mixture = Column(JSONB)
    
    strain = Column(ARRAY(Float))
    stress = Column(ARRAY(Float))
    
    duplicate_check_keys = ['name','peak_strain','peak_stress','elastic_modulus','possion_ratio','mixture','strain','stress']
    


class Source(Base):
    __tablename__ = 'source'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    author = Column(String)
    expOrsimu = Column(String)
    software = Column(String)
    device = Column(String)
    date = Column(Date)
    
    duplicate_check_keys = ['author','expOrsimu','software','device','date']
    
    
class Measurement(Base):
    
    __tablename__ = 'measurement'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String)
    expOrsimu = Column(String)
    physical_meaning = Column(String)
    description = Column(String)
    start_time = Column(Date)
    frequency = Column(Integer)
    data = Column(ARRAY(Float))
    
    duplicate_check_keys = ['name','expOrsimu','physical_meaning','description','start_time','frequency']
    
    
    