from pydantic import json
from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload


from db.session import get_db, async_session
from db.models import av_by_user, Car, City


@staticmethod
async def select_car():
    async with async_session() as s:
        car = s.execute(select(Car).order_by(Car.data_create.desc()))
        c = car.scalars().all()
        return c


@staticmethod
async def select_data():
    async with async_session() as session:
        query = select(av_by_user.name)
        result = session.execute(query)
        user = result.scalars().all()
        print(f'Users: \n {user}')

@staticmethod
async def select_user():
    async with async_session() as session:
        query = select(av_by_user)
        res = session.execute(query)
        return res.scalars().all()

@staticmethod
async def select_city():
    async with async_session() as s:
        query = select(City)
        res = s.execute(query)
        return res.scalars().all()

@staticmethod
async def get_car_id(id: int):
    async with async_session() as s:
        query = select(Car)
        res = s.execute(query.filter(Car.id == id))
        return res.scalars().first()

@staticmethod
async def get_car_ad(id: int):
    async with async_session() as s:
        query = select(Car)
        res = s.execute(query.filter(Car.user_id == id))
        return res.scalars().all()

@staticmethod
async def insert_user(user: dict):
    async with async_session() as s:
        query = insert(av_by_user).values(user)
        s.execute(query)
        s.commit()
    return f'Пользователь добавлен'

@staticmethod
async def select_car_page(page: int=1):
    async with async_session() as s:
        query = select(Car)
        d = s.execute(query.order_by(Car.data_create.desc()))
        r = d.scalars().all()[:10*page]
        return r

@staticmethod
async def insert_car(car: dict):
    async with async_session() as s:
        query = insert(Car).values(car)
        s.execute(query)
        s.commit()
        return {'statys': 'sucsess',
                'car': car,}

@staticmethod
async def userlogin(name: str, password: str):

    async with async_session() as session:
        query = (select(av_by_user.name, av_by_user.password).filter())
        res_query = session.execute(query)
        query_d = dict(res_query.all())

        try:
            if query_d[f'{name}'] == password:
                query_user = (select(av_by_user.id, av_by_user.name))
                res_query_user = session.execute(query_user)
                res = dict(res_query_user.all())
                for k, v in res.items():
                    if v == name:
                        return {'status': True, 'User_id': k, 'name': v}
            else:
                return {'status':False}
        except:
            return {'status': False}

@staticmethod
async def userreg(ph, n, p):
    async with async_session() as s:
        query_name = select(av_by_user.name)
        res_name = s.execute(query_name).scalars().all()
        if n in res_name:
            return {'status': False, 'mes': 'Такое имя уже есть. Придумайте другое' }
        stm = insert(av_by_user).values({'phone': ph,'name': n, 'password': p, 'hashed_password': p })
        s.execute(stm)
        s.commit()
        query_id = select(av_by_user.id).filter(av_by_user.name == n)
        k = s.execute(query_id).scalars().all()
        return {'status': True, 'User_id': k[0], 'name': n}