from fastapi import APIRouter, HTTPException, Depends
from app.models import Patient, PatientCreate, PatientUpdate
from app.database import create_db_and_tables, get_session
from sqlmodel import Session, select
from typing import Optional
from app.auth import get_current_user
from app.models import User

router = APIRouter(prefix="/patients", tags=["patients"])

Fake_DB: list[Patient] = [] 


@router.post("/", response_model= Patient, status_code = 201, tags= ['Patients'])
def create_patient(patient_in: PatientCreate, session: Session= Depends(get_session), user: User = Depends(get_current_user)):
    patient = Patient.model_validate(patient_in)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.get("/", response_model=list[Patient])
def get_patients(
    active: Optional[bool] = None,
    condition: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session)
):
    statement = select(Patient)

    if active is not None:
        statement = statement.where(Patient.active == active)

    if condition is not None:
        statement = statement.where(Patient.condition == condition)

    statement = statement.offset(offset).limit(limit)
    patients = session.exec(statement).all()
    return patients


@router.get("/{patient_id}", response_model= Patient, tags=["patients"])
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if patient:
        return patient
        
    raise HTTPException(status_code= 404, detail= "Patient not found")
         

@router.put("/{patient_id}", response_model=Patient, tags=["patients"])
def update_patient(patient_id: int, patient_in: PatientCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    got_patient = session.get(Patient, patient_id)
    if not got_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    got_patient.sqlmodel_update(patient_in.model_dump())
    session.add(got_patient)
    session.commit()
    session.refresh(got_patient)
    return got_patient

@router.patch("/{patient_id}", response_model = Patient, tags=["patients"])
def patch_patient(patient_id: int, patient_in: PatientUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    got_pat = session.get(Patient, patient_id)
    if not got_pat:
        raise HTTPException(status_code = 404, detail = "Patient not found")
    got_pat.sqlmodel_update(patient_in.model_dump(exclude_unset = True))
    session.add(got_pat)
    session.commit()
    session.refresh(got_pat)
    return got_pat
   

@router.delete("/{patient_id}", status_code = 204, tags=["patients"])
def delete_patient(patient_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code = 404, detail = "Patient not found")
    session.delete(patient)
    session.commit()
    return

