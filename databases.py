from typing import Optional

from sqlalchemy.ext.asynco import create_async_engine, asynco_sessionmaker, engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = asynco_sessionmaker(engine, expire_on_commit=True)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.mtadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.mtadata.create_all)