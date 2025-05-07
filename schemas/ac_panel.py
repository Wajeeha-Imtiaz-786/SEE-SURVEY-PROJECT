from pydantic import BaseModel
from typing import Optional, List
from .ac_panel_cb_load import ACPanelCBLoadOut

class ACPanelBase(BaseModel):
    length_power_cable_from_meter_m: Optional[float]
    cross_section_cable_from_meter_mm2: Optional[float]
    ac_panel_main_cb_rating_amp: Optional[float]
    ac_panel_main_cb_type: Optional[str]
    has_free_cbs: Optional[str]
    free_space_to_add_new_cbs: Optional[int]

class ACPanelCreate(ACPanelBase):
    site_session_id: int

class ACPanelOut(ACPanelBase):
    id: int
    site_session_id: int
    cbs_loads: List[ACPanelCBLoadOut] = []

    class Config:
        from_attributes = True  # Updated from 'orm_mode'
        validate_by_name = True  # Updated from 'allow_population_by_field_name'
