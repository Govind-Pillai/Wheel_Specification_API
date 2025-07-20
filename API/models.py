from sqlalchemy import Column, String, Date, JSON
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    form_number = Column(String, primary_key=True, index=True)
    submitted_by = Column(String, index=True)
    submitted_date = Column(Date)
    fields = Column(JSON)
