from pydantic import BaseModel
from typing import Optional, List
from .ac_panel_cb_load import ACPanelCBLoadOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

class ACPanelBase(BaseModel):
    length_power_cable_from_meter_m: Optional[float]
    cross_section_cable_from_meter_mm2: Optional[float]
    ac_panel_main_cb_rating_amp: Optional[float]
    ac_panel_main_cb_type: Optional[str]
    has_free_cbs: Optional[str]
    free_space_to_add_new_cbs: Optional[int]

class ACPanelCreate(BaseModel):
    name: str
    description: str
    capacity: float

class ACPanelResponse(BaseModel):
    id: int
    name: str
    description: str
    capacity: float

    class Config:
        from_attributes = True

class ACPanelOut(ACPanelBase):
    id: int
    site_session_id: int
    cbs_loads: List[ACPanelCBLoadOut] = []

    class Config:
        from_attributes = True


