
from fastapi import FastAPI

app = FastAPI()


mevalar = ["banan", "olma", "nok", "shaftoli", "ananas"]




@app.get("/mevalar")
def mevalar_page(meva_nomi: str = ""):
    resp = {
        "message": "ok",
        "data": mevalar
    }
    if meva_nomi != "":
        resp["data"] = []
        for meva in mevalar:
            if meva.endswith(meva_nomi):
                resp["data"].append(meva)
    return resp    




@app.get("/mevalar/{meva_id}")
def meva_detail_page(meva_id: int):
    return {
        "message": "ok",
        "meva": mevalar[meva_id]
    } 


@app.post("/mevalar/create/")
def meva_yaratish_paage(meva_nomi: str):
    print(meva_nomi)
    mevalar.append(meva_nomi)
    return {"message": "meva yaratildi"}


@app.delete("/mevalar/{meva_id}/delete")
def meva_delete_page(meva_id: int):
    mevalar.pop(meva_id)
    return {"message": "meva ochirildi"}


@app.patch("/mevalar/{meva_id}/update")
def meva_update_page(meva_id: int, yangi_nom: str):
    mevalar[meva_id] = yangi_nom
    return {"message": "meva ozgartirildi"}


mashinalar = ["BMW", "MERS", "TAYOTA", "CHEVROLET", "MALIBU"]

@app.get("/mashinalar")
def mashinalar_page():
    return {
        "message": "ok",
        "data": mashinalar
    }

       

@app.get("/mashinalar/{mashina_id}")
def mashina_detial_page(mashina_id: int):
    return {
        "message": "ok",
        "data": mashinalar[mashina_id]
    }





@app.get("/")
def home_page():
    return {"message": "hello world"}


@app.get("/python")
def python_page():
    return {"message": "bu dasturlash tili"}


@app.get("/xato")
def xato_page():
    return {"error": "bu xato responce"}


