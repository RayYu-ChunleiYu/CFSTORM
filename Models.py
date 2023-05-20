from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship,declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class Experiment(Base):
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specimen_id = Column(Integer, ForeignKey('specimen.id'))
    specimen = relationship("Specimen", back_populates="experiment")
    
    load_pattern = Column(JSONB)
    data = Column(JSONB)
    
    source_id = Column(Integer, ForeignKey('source.id'))
    source = relationship("Source", back_populates="experiment")
    
class Specimen(Base):
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experiment = relationship("Experiment", back_populates="specimen")
    geometry_id = Column(Integer, ForeignKey('geometry.id'))
    geometry = relationship("Geometry", back_populates="specimens")
    material_id = Column(Integer, ForeignKey('material.id'))
    material = relationship("Material", back_populates="specimens")

class Geometry(Base):
    __tablename__ = 'geometry'
    id = Column(Integer, primary_key=True)
    specimens = relationship("Specimen", back_populates="geometry")
    
    section_type = Column(String)
    section_detail = Column(JSONB)
    length = Column(Float)
    
class Material(Base):
    __tablename__ = 'material'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specimens = relationship("Specimen", back_populates="material")
    
    detail = Column(JSONB)
    
    
class Source(Base):
    __tablename__ = 'source'
    
    id = Column(Integer, primary_key=True)
    detail = Column(JSONB)
    
    experiment = relationship("Experiment", back_populates="source")
    
    
    