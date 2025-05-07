from pydantic import BaseModel

class ACPanelCBLoadBase(BaseModel):
    label: str
    capacity_rate: float

class ACPanelCBLoadCreate(ACPanelCBLoadBase):
    ac_panel_id: int

class ACPanelCBLoadOut(ACPanelCBLoadBase):
    id: int
    ac_panel_id: int

    class Config:
        from_attributes = True  # Updated from 'orm_mode'
        validate_by_name = True  # Updated from 'allow_population_by_field_name'
