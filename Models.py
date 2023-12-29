from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
Base = declarative_base()


class MyMagic(Base):
    __abstract__ = True

    def __repr__(self):
        if "name" in self.__dict__:
            return "<MyMagic(id='%s', name='%s')>" % (self.id, self.name)
        else:
            return "<MyMagic(id='%s')>" % (self.id)


class Experiment(MyMagic):
    """
    Properties
    ----------

    name = Column(String)

    expOrsimu = Column(String)

    specimen_id = Column(Integer)

    load_pattern = Column(JSONB)

    measurements_id = Column(ARRAY(Integer))

    source_id = Column(Integer)

    key_features = Column(JSONB)

    notation = Column(String)
    """
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    expOrsimu = Column(String)
    specimen_id = Column(Integer)

    load_pattern = Column(String)
    load_pattern_details = Column(JSONB)
    measurements_id = Column(ARRAY(Integer))
    source_id = Column(Integer)
    key_features = Column(JSONB)
    notation = Column(String)
    duplicate_check_keys = [
        'name', 'expOrsimu', 'specimen_id', 'load_pattern', "load_pattern_details", 'measurements_id',
        'source_id', "key_features", 'notation']


class Specimen(MyMagic):
    """
    Properties
    ----------

    name = Column(String)

    geometry_id = Column(Integer)

    steel_id = Column(Integer)

    concrete_id = Column(Integer)

    notation = Column(String)


    """
    __tablename__ = 'specimen'
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    geometry_id = Column(Integer)
    steel_id = Column(Integer)
    concrete_id = Column(Integer)

    notation = Column(String)

    duplicate_check_keys = ['name', 'geometry_id', 'steel_id', 'concrete_id', 'notation']


class Geometry(MyMagic):
    """
    Properties
    ----------

    section_type = Column(String)

    section_width = Column(Float)

    section_height = Column(Float)

    section_diameter = Column(Float)

    steel_tube_thickness = Column(Float)

    length = Column(Float)

    """
    __tablename__ = 'geometry'
    id = Column(Integer, primary_key=True, autoincrement=False)
    section_type = Column(String)
    section_width = Column(Float)
    section_height = Column(Float)
    section_diameter = Column(Float)
    section_steel_tube_thickness = Column(Float)
    length = Column(Float)
    notation = Column(String)

    duplicate_check_keys = [
        'section_type',
        'section_width', 'section_height', 'section_diameter', "section_steel_tube_thickness",
        'length', 'notation']


class Steel(MyMagic):
    """
    Properties
    ----------
    name = Column(String)

    yield_strength = Column(Float)

    yield_strain = Column(Float)

    elastic_modulus = Column(Float)

    ultimate_strength = Column(Float)

    ultimate_strain = Column(Float)

    possion_ratio = Column(Float)

    strain = Column(ARRAY(Float))

    stress = Column(ARRAY(Float))
    """
    __tablename__ = 'steel'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    yield_strength = Column(Float)
    yield_strain = Column(Float)
    elastic_modulus = Column(Float)
    ultimate_strength = Column(Float)
    ultimate_strain = Column(Float)
    possion_ratio = Column(Float)
    strain = Column(ARRAY(Float))
    stress = Column(ARRAY(Float))
    notation = Column(String)

    duplicate_check_keys = ['name',
                            'yield_strength', 'yield_strain',
                            'elastic_modulus',
                            'ultimate_strength', 'ultimate_strain',
                            'possion_ratio',
                            'strain', 'stress',
                            'notation']


class Concrete(MyMagic):
    """
    Properties
    ----------
    name = Column(String)

    peak_strain = Column(Float)

    peak_stress = Column(Float)

    elastic_modulus = Column(Float)

    possion_ratio = Column(Float)

    mixture = Column(JSONB)

    strain = Column(ARRAY(Float))

    stress = Column(ARRAY(Float))
    """
    __tablename__ = 'concrete'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    compressive_peak_strain = Column(Float)
    compressive_peak_stress = Column(Float)
    elastic_modulus = Column(Float)
    possion_ratio = Column(Float)
    tensile_peak_strain = Column(Float)
    tensile_peak_stress = Column(Float)
    mixture = Column(JSONB)
    strain = Column(ARRAY(Float))
    stress = Column(ARRAY(Float))
    notation = Column(String)

    duplicate_check_keys = ['name', 'compressive_peak_strain', 'compressive_peak_stress',
                            'elastic_modulus', 'possion_ratio',
                            "tensile_peak_strain", "tensile_peak_stress",
                            "mixture",
                            'strain', 'stress',
                            'notation']


class Source(MyMagic):
    """
    Properties
    ----------
    author = Column(String)

    software = Column(String)

    device = Column(String)

    date = Column(Date)

    """
    __tablename__ = 'source'
    id = Column(Integer, primary_key=True, autoincrement=False)
    author = Column(String)
    software = Column(String)
    device = Column(String)
    date = Column(DateTime)

    notation = Column(String)

    duplicate_check_keys = ['author', 'software', 'device', 'date', 'notation']


class Measurement(MyMagic):
    """
    Properties
    ----------
    name = Column(String)

    notation = Column(String)

    start_time = Column(Date)

    frequency = Column(Integer)

    data = Column(JSONB)

    """
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)

    start_time = Column(DateTime)
    frequency = Column(Integer)
    time = Column(ARRAY(DateTime))
    data = Column(JSONB)

    notation = Column(String)

    duplicate_check_keys = ['name', 'start_time', 'frequency', 'notation']
