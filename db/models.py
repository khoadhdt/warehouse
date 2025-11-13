# warehouse_app/db/models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class InventoryEntryCreate(BaseModel):
    component_id: str
    component_name: str
    group_name: Optional[List[str]] = []
    process: Optional[List[str]] = []
    model: Optional[List[str]] = []
    size: str
    unit: Optional[str] = None
    team_id: int
    material: Optional[List[str]] = []
    storage_location: Optional[str] = None
    invoice: str
    modinvoice: str
    status: Optional[str] = None
    note: str
    quantity: float
    movement_type: str = "adjustment"
    created_by: int
