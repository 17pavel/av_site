from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from db.session import async_session

from db.models import Favorites, MessagesCar


async def insert_favorite(user_id: int, car_id: int):
    async with async_session() as s:
        query = insert(Favorites).values({'user_id': user_id, 'car_id': car_id})
        s.execute(query)
        s.commit()
    return f'Машина добавлена в избранное'


async def select_favorite(user_id: int):
    async with async_session() as s:
        query = select(Favorites).filter(Favorites.user_id == user_id).options(joinedload(Favorites.car))
        fav = s.execute(query).scalars().all()
        return fav


async def insert_mes(mes):
    async with async_session() as s:
        query = insert(MessagesCar).values(mes)
        s.execute(query)
        s.commit()
    return f'Сообщение отправлено'


async def select_message(id: int):
    async with async_session() as s:
        query = select(MessagesCar).filter(MessagesCar.user_id == id).options(joinedload(MessagesCar.carmes)).options(
            joinedload(MessagesCar.usermes)).order_by(MessagesCar.car_id)
        r = s.execute(query).scalars().all()
        return r


async def sel_mes_owner(id: int):
    async with async_session() as s:
        query = select(MessagesCar).options(joinedload(MessagesCar.carmes))
        r = s.execute(query).scalars().all()
        return r
