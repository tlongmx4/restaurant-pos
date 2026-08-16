from sqlalchemy import Column, ForeignKey, Numeric, String
from app.db import base

class MenuItem(base):
    __tablename__ = "menu_items"

    id = Column(Numeric, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric(precision=6, scale=2))