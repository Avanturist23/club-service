from app.api.models import ClubIn, ClubOut
from app.api.db import clubs, database


async def add_club(payload: ClubIn):
    query = clubs.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_club():
    query = clubs.select()
    return await database.fetch_all(query=query)


async def get_club(id):
    query = clubs.select().where(clubs.c.id == id)
    return await database.fetch_one(query=query)


async def delete_club(id: int):
    query = clubs.delete().where(clubs.c.id == id)
    return await database.execute(query=query)

