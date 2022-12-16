"""  Connection declaration  """
import datetime
from .models import Base, Statistic
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine('sqlite+aiosqlite://')


async def create_tables_and_rows():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSession(engine) as session:
        async with session.begin():
            session.add_all(
                [
                    Statistic(date=datetime.datetime(2018, 11, 1), views=130, clicks=12467, cost=3.1233),
                    Statistic(date=datetime.datetime(2016, 11, 1), views=42, clicks=56856, cost=2.3423),
                    Statistic(date=datetime.datetime(2005, 11, 1), views=2345, clicks=3456, cost=5.2323),
                    Statistic(date=datetime.datetime(2017, 11, 1), views=5346, clicks=23456, cost=6.12343),
                    Statistic(date=datetime.datetime(2015, 11, 1), views=1234, clicks=2325, cost=23.23563),
                    Statistic(date=datetime.datetime(2012, 11, 1), views=113, clicks=3456, cost=5.2463),
                    Statistic(date=datetime.datetime(2011, 11, 1), views=124, clicks=123, cost=6.34563),
                    Statistic(date=datetime.datetime(2014, 11, 1), views=12, clicks=234678, cost=2.65793),
                    Statistic(date=datetime.datetime(2012, 6, 1), views=673, clicks=24, cost=1.7893),
                    Statistic(date=datetime.datetime(2015, 12, 1), views=256, clicks=12345, cost=3.453),
                ]
            )
