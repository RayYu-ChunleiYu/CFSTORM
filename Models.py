from sqlalchemy import Column, Integer, Float, String, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship,declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class Experiment(Base):
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specimen_id = Column(Integer)
    
    load_pattern = Column(JSONB)
    data = Column(JSONB)
    
    source_id = Column(Integer)
    
    __table_args__ = (UniqueConstraint('name', 'specimen_id','load_pattern','data','source_id'),)
    
class Specimen(Base):
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geometry_id = Column(Integer)
    material_id = Column(Integer)
    
    
    __table_args__ = (UniqueConstraint('name', 'geometry_id','material_id',),)
    

class Geometry(Base):
    __tablename__ = 'geometry'
    id = Column(Integer, primary_key=True)
    
    section_type = Column(String)
    section_detail = Column(JSONB)
    length = Column(Float)
    
    __table_args__ = (UniqueConstraint('section_type', 'section_detail','length',),)
    
    
class Material(Base):
    __tablename__ = 'material'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    detail = Column(JSONB)
    
    __table_args__ = (UniqueConstraint('name', 'detail',),)
    
    
    
class Source(Base):
    __tablename__ = 'source'
    
    id = Column(Integer, primary_key=True)
    detail = Column(JSONB)
    
    
    __table_args__ = (UniqueConstraint('detail',),)
    
    
    
    