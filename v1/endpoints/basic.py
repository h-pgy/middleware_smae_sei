
from fastapi import APIRouter, Depends, HTTPException

from fastapi_pagination import Page, add_pagination, paginate

import core.dao.basic as dao
import core.schemas.basic as schemas


app = APIRouter()

@app.get("/unidades", response_model=Page[schemas.Unidade], tags=['parametros_do_processo'])
def get_unidades():

    unidades = dao.lst_unidades()
    return paginate(unidades)


add_pagination(app)


