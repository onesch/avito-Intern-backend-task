from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_or_404(db: Session, model, obj_id: int, name: str):
    obj = db.get(model, obj_id)
    if not obj:
        raise HTTPException(
            status_code=404,
            detail=f"{name} not found."
        )
    return obj
