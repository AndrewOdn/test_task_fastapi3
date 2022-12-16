from typing import Optional, Literal, Union
from datetime import datetime
from pydantic import BaseModel, validator


class PostStatistic(BaseModel):
    """POST body:: api/v1/statistic request validation model"""
    date: str
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None

    @validator("date", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        )


class GetStatistic(BaseModel):
    """GET query:: api/v1/statistic request validation model"""
    from_date: Optional[Union[str, None]] = None
    to_date: Optional[Union[str, None]] = None
    sort_by: Optional[Literal[
        "date",
        "views",
        "clicks",
        "cost",
        "cpc",
        "cpm",
    ]] = 'date'
    sort_type: Optional[Literal[
        "asc",
        "desc",
    ]] = 'asc'

    @validator("from_date", "to_date")
    def parse_birthdate(cls, value):
        if value:
            return datetime.strptime(
                value,
                "%Y-%m-%d"
            )
