from typing import Optional, Literal, Union, List
from datetime import datetime
from pydantic import BaseModel, validator


class GoodStatus(BaseModel):
    """Base response body"""

    State: Literal["Ok"]


class Statistic_shema(BaseModel):
    """GET body:: api/v1/statistic response validation model"""

    date: Union[datetime, None]
    views: Union[int, None]
    clicks: Union[int, None]
    cost: Union[float, None]
    cpc: Union[float, None]
    cpm: Union[float, None]


class SendStatistic(BaseModel):
    """GET body:: api/v1/statistic response validation model"""

    __root__: List[Statistic_shema]


class PostStatistic(BaseModel):
    """POST body:: api/v1/statistic request validation model"""

    date: str
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None

    @validator("date")
    def parse_birthdate(cls, value: str) -> datetime:
        return datetime.strptime(value, "%Y-%m-%d")


class GetStatistic(BaseModel):
    """GET query:: api/v1/statistic request validation model"""

    from_date: Optional[Union[str, None]] = None
    to_date: Optional[Union[str, None]] = None
    sort_by: Optional[
        Literal[
            "date",
            "views",
            "clicks",
            "cost",
            "cpc",
            "cpm",
        ]
    ] = "date"
    sort_type: Optional[
        Literal[
            "asc",
            "desc",
        ]
    ] = "asc"

    @validator("from_date", "to_date")
    def parse_birthdate(cls, value: object) -> datetime:
        if value:
            return datetime.strptime(value, "%Y-%m-%d")
