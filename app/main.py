
from fastapi import FastAPI
from app.dataprev import consultar_contrato_api

app = FastAPI()

@app.post("/consultar-contrato")
async def consultar_contrato(contrato: list[str]):

    resultados = []

    for c in contrato:
        resultado = await consultar_contrato_api(c)
        resultados.append(resultado)
    return {"resultados": resultados}
