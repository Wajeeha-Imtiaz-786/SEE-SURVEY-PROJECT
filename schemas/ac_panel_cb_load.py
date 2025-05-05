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
        orm_mode = True
