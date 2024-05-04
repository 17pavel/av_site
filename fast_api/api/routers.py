# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from ..api.schemas import *
# from ..db.session import get_db
#
# user_router = APIRouter()
#
#
# async def _create_new_user(body: UserCreate, db) -> ShowUser:
#     async with db as session:
#         async with session.begin():
#             user_dal = UserDAL(session)
#             user = await user_dal.create_user(
#                 name=body.name,
#                 surname=body.surname,
#                 email=body.email,
#             )
#             return ShowUser(
#                 user_id=user.user_id,
#                 name=user.name,
#                 surname=user.surname,
#                 email=user.email,
#                 is_active=user.is_active,
#             )
#
#
# @user_router.post("/", response_model=ShowUser)
# async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)):
#     return await _create_new_user(body, db)
from fastapi import APIRouter

from ..api.schemas import UserAuthDTO, UserFavDTO, UserRegDTO
from ..db.models import av_by_user
from ..orm import select_user, select_city, select_car, get_car_id, insert_user, select_car_page, insert_car, \
    userlogin, get_car_ad, userreg
from ..orm_user import insert_favorite, select_favorite, insert_mes, select_message, sel_mes_owner

router = APIRouter()

@router.get('/city/')
def get_city():
    c = select_city()
    return c

@router.get('/car/')
def get_car():
    car = select_car()
    return car

@router.get('/car/{id}')
def get_car(id:int):
    car = get_car_id(id)
    return car

@router.get('/user/')
def get_user():
    user = select_user()
    return user

@router.get('/carpage/{page}')
def get_car(page:int =1):
    car = select_car_page(page)
    return car

@router.get('/user/ad/{id}')
def get_user_ad(id:int):
    ad = get_car_ad(id)
    return ad

@router.post('/user/')
def create_user(user:dict):
    r = insert_user(user)
    return r

@router.post('/userlogin/')
def user_login(user: UserAuthDTO):
    n = user.name
    p = user.password
    res = userlogin(n, p)
    return res
@router.post('/car/')
def create_car(car:dict):
    r = insert_car(car)
    return r

@router.post('/user/favorit/')
def create_favorite_car(Fav: UserFavDTO):
    us = Fav.user_id
    c = Fav.car_id
    r = insert_favorite(us,c)
    return r

@router.get('/user/favorite/{id}')
def get_favorite_car(id:int):
    r = select_favorite(id)
    res = list()
    for i in r:
        res.append(i.car)
    return res

@router.post('/user/mes')
def create_mes(mes: dict):
    r = insert_mes(mes)
    return r

@router.post('/userreg/')
def User_reg(reg:UserRegDTO):
    ph = reg.phone
    n = reg.name
    p = reg.password
    r = userreg(ph, n, p)
    return r

@router.get('/user/message/{id}')
def get_message(id: int):
    r = select_message(id)
    return r

@router.get('/user/message/owner/{id}')
def get_owner(id: int):
    r = sel_mes_owner(id)
    return r