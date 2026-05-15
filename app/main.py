from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from app.dataprev import DataprevBrowser


browser = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global browser

    browser = DataprevBrowser()

    yield

    browser.close()


app = FastAPI(lifespan=lifespan)

class ContratosRequest(BaseModel):
    contratos: list[str]


@app.post("/consultar-contrato")
async def consultar_contrato(req: ContratosRequest):

    resultados = []

    for c in req.contratos:
        resultado = browser.consultar(c)
        resultados.append(resultado)

    return {"resultados": resultados}