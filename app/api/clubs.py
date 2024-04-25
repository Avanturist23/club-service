from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import ClubOut, ClubIn
from app.api import db_manager

clubs = APIRouter()

@clubs.post('/', response_model=ClubOut, status_code=201)
async def create_club(payload: ClubIn):
    club_id = await db_manager.add_club(payload)

    response = {
        'id': club_id,
        **payload.dict()
    }

    return response


@clubs.get('/', response_model=List[ClubOut])
async def get_clubs():
    return await db_manager.get_all_club()


@clubs.get('/{id}/', response_model=ClubOut)
async def get_club(id: int):
    company = await db_manager.get_club(id)
    if not company:
        raise HTTPException(status_code=404, detail="club not found")
    return company


@clubs.delete('/{id}/', response_model=None)
async def delete_club(id: int):
    company = await db_manager.get_club(id)
    if not company:
        raise HTTPException(status_code=404, detail="club not found")
    return await db_manager.delete_club(id)