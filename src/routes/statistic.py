from fastapi import APIRouter, Depends
from ..schemas.statistic import PostStatistic, GetStatistic
from ..sql.query.statistic import delete_statistic_table, select_statistic, update_statistic_row

router = APIRouter(prefix='/api/v1', tags=['Statistic'])


@router.get("/statistic", status_code=200)
async def get_statistic(query: GetStatistic = Depends()):
    return await select_statistic(query)


@router.post("/statistic", status_code=201)
async def add_statistic(body: PostStatistic):
    await update_statistic_row({"date": body.date, "views": body.views, "clicks": body.clicks, "cost": body.cost})
    return {"State": "Ok"}


@router.delete("/statistic")
async def delete_statistic_all():
    await delete_statistic_table()
    return {"State": "Ok"}
