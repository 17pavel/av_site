import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import BaseModel
from sqlalchemy import MetaData, ForeignKey, text, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import Annotated



class Base(DeclarativeBase):
    metadata = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]

class av_by_user(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'av_by_user'
    id: Mapped[intpk]
    name: Mapped[str]
    phone: Mapped[str]
    photo: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[str] = mapped_column(
        String(length=320), index=True, nullable=True,
        )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    car: Mapped['Car'] = relationship(
        back_populates='user'
    )

    favorit: Mapped['Favorites'] = relationship(
        back_populates='user'
    )
    mes: Mapped['MessagesCar'] = relationship(
        back_populates='usermes'
    )

class City(Base):
    __tablename__ = 'av_by_city'
    id: Mapped[intpk]
    name: Mapped[str]
    region: Mapped[str]

    car: Mapped['Car'] = relationship(
        back_populates='city'
    )


class Car(Base):
    __tablename__ = 'av_by_car'
    id: Mapped[intpk]
    mark_car: Mapped[str]
    model_car: Mapped[str]
    generation: Mapped[str]
    body: Mapped[str]
    motor: Mapped[str]
    transmission: Mapped[str]
    drive: Mapped[str]
    year: Mapped[int]
    price: Mapped[int]
    volume: Mapped[str]
    photo: Mapped[str]
    vin: Mapped[str] = mapped_column(nullable=True)
    data_create: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    mileage: Mapped[int]
    color: Mapped[str]
    condition: Mapped[str]
    description: Mapped[str]
    exchange: Mapped[str]
    options: Mapped[str] = mapped_column(nullable=True)
    city_id_id: Mapped[int] = mapped_column(ForeignKey('av_by_city.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('av_by_user.id'))

    city: Mapped['City'] = relationship(
        back_populates='car'
    )

    user: Mapped['av_by_user'] = relationship(
        back_populates='car'
    )
    favorites: Mapped['Favorites'] = relationship(
        back_populates='car'
    )
    mes: Mapped['MessagesCar'] = relationship(
        back_populates='carmes'
    )

class Favorites(Base):
    __tablename__ = 'favorites'
    id: Mapped[intpk]
    car_id: Mapped[int] = mapped_column(ForeignKey('av_by_car.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('av_by_user.id'))
    car: Mapped['Car'] = relationship(
        back_populates='favorites'
    )
    user: Mapped['av_by_user'] = relationship(
        back_populates='favorit'
    )

class MessagesCar(Base):
    __tablename__ = 'messagescar'
    id: Mapped[intpk]
    text: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('av_by_user.id'))
    owner_id: Mapped[int] = mapped_column(default=72)
    car_id: Mapped[int] = mapped_column(ForeignKey('av_by_car.id'))
    open: Mapped[bool] = mapped_column(default=False)
    carmes: Mapped['Car'] = relationship(
        back_populates='mes'
    )
    usermes: Mapped['av_by_user'] = relationship(
        back_populates='mes'
    )