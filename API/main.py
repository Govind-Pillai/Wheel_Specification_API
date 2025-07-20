from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from . import models, database

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for input
class WheelInput(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: dict

@app.post("/api/forms/wheel-specifications")
def submit_wheel_spec(wheel: WheelInput, db: Session = Depends(get_db)):
    # Check if already exists
    existing = db.query(models.WheelSpecification).filter_by(form_number=wheel.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail="Form already submitted.")

    # Save to DB
    wheel_data = models.WheelSpecification(
        form_number=wheel.formNumber,
        submitted_by=wheel.submittedBy,
        submitted_date=datetime.strptime(wheel.submittedDate, "%Y-%m-%d").date(),
        fields=wheel.fields
    )
    db.add(wheel_data)
    db.commit()
    db.refresh(wheel_data)

    # Return response
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": wheel.formNumber,
            "submittedBy": wheel.submittedBy,
            "submittedDate": wheel.submittedDate,
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications")
def get_wheel_spec(
    formNumber: str = Query(...),
    submittedBy: str = Query(...),
    submittedDate: str = Query(...),
    db: Session = Depends(get_db)
):
    # Query the DB for matching record
    record = db.query(models.WheelSpecification).filter_by(
        form_number=formNumber,
        submitted_by=submittedBy,
        submitted_date=submittedDate
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Wheel specification not found.")

    # Response
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [
            {
                "formNumber": record.form_number,
                "submittedBy": record.submitted_by,
                "submittedDate": str(record.submitted_date),
                "fields": {
                    "treadDiameterNew": record.fields.get("treadDiameterNew"),
                    "lastShopIssueSize": record.fields.get("lastShopIssueSize"),
                    "condemningDia": record.fields.get("condemningDia"),
                    "wheelGauge": record.fields.get("wheelGauge")
                }
            }
        ]
    }

@app.get("/")
def index():
    return {"message": "Hello FASTAPI"}
