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

# Added ACPanelsCBLoadCreate class to represent the creation model for AC panel CB loads
class ACPanelsCBLoadCreate(BaseModel):
    label: str
    capacity_rate: float
    ac_panel_id: int

# Added ACPanelsCBLoadResponse class to represent the response model for AC panel CB loads
class ACPanelsCBLoadResponse(BaseModel):
    id: int
    label: str
    capacity_rate: float
    ac_panel_id: int

    class Config:
        from_attributes = True
