import uuid
# import sqlalchemy as sa
from sqlalchemy import JSON, Boolean, Column, Float, ForeignKey, Integer, MetaData, String, Table
# from sqlalchemy.engine import URL
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

##############################
# BLOCK WITH DATABASE MODELS #
##############################

Base = declarative_base()
metadata = Base.metadata

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("link", String),
    Column("name", String),
    Column("price", Float),
    Column("brand", ForeignKey("brand.id")),
    Column("model", ForeignKey("model.id")),
    Column("category", ForeignKey("category.id")),
    Column("parameters", JSON),
)

category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

brand = Table(
    "brand",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

model = Table(
    "model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("brand", ForeignKey("brand.id")),
)

images = Table(
    "images",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("link", String),
    Column("item", ForeignKey("items.id")),
)


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
