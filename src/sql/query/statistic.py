import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from ..connection import engine
from ..models import Statistic


async def delete_statistic_table():
    async with AsyncSession(engine) as session:
        async with session.begin():
            await session.execute(sa.delete(Statistic))


async def update_statistic_row(row):
    async with AsyncSession(engine) as session:
        async with session.begin():
            pre_commit = await session.execute(sa.select(Statistic).where(Statistic.date == row['date']))
            if pre_commit.scalars().first():
                date = row.pop("date")
                await session.execute(sa.update(Statistic).where(Statistic.date == date).values(row))
            else:
                await session.execute(sa.insert(Statistic).values(row))


async def select_statistic(params):
    async with AsyncSession(engine) as session:
        async with session.begin():
            query = sa.select(Statistic.date, Statistic.views, Statistic.cost, Statistic.clicks,
                              (Statistic.cost / Statistic.clicks).label('cpc'),
                              (Statistic.cost / Statistic.views * 1000).label('cpm'))
            order_part = Statistic.date
            if params.from_date:
                query = query.where(Statistic.date >= params.from_date)
            if params.to_date:
                query = query.where(Statistic.date <= params.to_date)
            if params.sort_by == "views":
                order_part = Statistic.views
            elif params.sort_by == "clicks":
                order_part = Statistic.clicks
            elif params.sort_by == "cost":
                order_part = Statistic.cost
            elif params.sort_by == "cpc":
                order_part = (Statistic.cost / Statistic.clicks).label('cpc')
            elif params.sort_by == "cpm":
                order_part = (Statistic.cost / Statistic.views).label('cpm')
            if params.sort_type == 'desc':
                order_part = order_part.desc()
            result = await session.execute(query.order_by(order_part))
            return result.mappings().all()
