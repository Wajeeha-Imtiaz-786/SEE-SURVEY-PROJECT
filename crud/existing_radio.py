from sqlalchemy.orm import Session
from models import existing_radio as models
from schemas import existing_radio as schemas

# 1. Antenna Structure Info CRUD

def create_antenna_structure_info(db: Session, data: schemas.AntennaStructureInfoCreate):
    data_dict = data.dict()
    data_dict['tower_type'] = ','.join(data_dict['tower_type'])
    if data_dict.get('rt_existing_heights'):
        data_dict['rt_existing_heights'] = ','.join(data_dict['rt_existing_heights'])
    obj = models.AntennaStructureInfo(**data_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_antenna_structure_info(db: Session, site_session_id: int):
    return db.query(models.AntennaStructureInfo).filter_by(site_session_id=site_session_id).all()

def update_antenna_structure_info(db: Session, id: int, data: dict):
    obj = db.query(models.AntennaStructureInfo).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_antenna_structure_info(db: Session, id: int):
    obj = db.query(models.AntennaStructureInfo).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 2. MW Antennas CRUD

def create_mw_antenna(db: Session, data: schemas.MWAntennasCreate):
    obj = models.MWAntennas(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_mw_antennas(db: Session, site_session_id: int):
    return db.query(models.MWAntennas).filter_by(site_session_id=site_session_id).all()

def update_mw_antenna(db: Session, id: int, data: dict):
    obj = db.query(models.MWAntennas).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_mw_antenna(db: Session, id: int):
    obj = db.query(models.MWAntennas).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 3. External DC PDU CRUD

def create_external_dc_pdu(db: Session, data: schemas.ExternalDCPDUCreate):
    obj = models.ExternalDCPDU(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_external_dc_pdus(db: Session, site_session_id: int):
    return db.query(models.ExternalDCPDU).filter_by(site_session_id=site_session_id).all()

def update_external_dc_pdu(db: Session, id: int, data: dict):
    obj = db.query(models.ExternalDCPDU).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_external_dc_pdu(db: Session, id: int):
    obj = db.query(models.ExternalDCPDU).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 3.1. DC PDU CB/Fuse CRUD

def create_dcpdu_cb_fuse(db: Session, data: schemas.DCPDUCBFuseCreate):
    obj = models.DCPDUCBFuse(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_dcpdu_cb_fuses(db: Session, pdu_id: int):
    return db.query(models.DCPDUCBFuse).filter_by(pdu_id=pdu_id).all()

def update_dcpdu_cb_fuse(db: Session, id: int, data: dict):
    obj = db.query(models.DCPDUCBFuse).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_dcpdu_cb_fuse(db: Session, id: int):
    obj = db.query(models.DCPDUCBFuse).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 4. Radio Antennas CRUD

def create_radio_antenna(db: Session, data: schemas.RadioAntennaCreate):
    data_dict = data.dict()
    data_dict['technology'] = ','.join(data_dict['technology'])
    if data_dict.get('other_vendor_port_type'):
        data_dict['other_vendor_port_type'] = ','.join(data_dict['other_vendor_port_type'])
    if data_dict.get('other_vendor_bands'):
        data_dict['other_vendor_bands'] = ','.join(data_dict['other_vendor_bands'])
    if data_dict.get('other_vendor_bands_supported_by_free_ports'):
        data_dict['other_vendor_bands_supported_by_free_ports'] = ','.join(data_dict['other_vendor_bands_supported_by_free_ports'])
    obj = models.RadioAntenna(**data_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_radio_antennas(db: Session, site_session_id: int):
    return db.query(models.RadioAntenna).filter_by(site_session_id=site_session_id).all()

def update_radio_antenna(db: Session, id: int, data: dict):
    obj = db.query(models.RadioAntenna).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_radio_antenna(db: Session, id: int):
    obj = db.query(models.RadioAntenna).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 5. Radio Units CRUD

def create_radio_unit(db: Session, data: schemas.RadioUnitCreate):
    data_dict = data.dict()
    if data_dict.get('dc_cb_fuse'):
        data_dict['dc_cb_fuse'] = ','.join(data_dict['dc_cb_fuse'])
    obj = models.RadioUnit(**data_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_radio_units(db: Session, site_session_id: int):
    return db.query(models.RadioUnit).filter_by(site_session_id=site_session_id).all()

def update_radio_unit(db: Session, id: int, data: dict):
    obj = db.query(models.RadioUnit).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_radio_unit(db: Session, id: int):
    obj = db.query(models.RadioUnit).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# 5.1. Radio Unit Port Connectivity CRUD

def create_radio_unit_port_connectivity(db: Session, data: schemas.RadioUnitPortConnectivityCreate):
    obj = models.RadioUnitPortConnectivity(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_radio_unit_port_connectivities(db: Session, radio_unit_id: int):
    return db.query(models.RadioUnitPortConnectivity).filter_by(radio_unit_id=radio_unit_id).all()

def update_radio_unit_port_connectivity(db: Session, id: int, data: dict):
    obj = db.query(models.RadioUnitPortConnectivity).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_radio_unit_port_connectivity(db: Session, id: int):
    obj = db.query(models.RadioUnitPortConnectivity).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
