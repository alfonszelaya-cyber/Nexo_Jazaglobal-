from fastapi import FastAPI

app = FastAPI(title="ZYRA NEXO CORE")

@app.get("/")
def root():
    return {
        "system": "ZYRA_NEXO_CORE",
        "status": "running"
    }

@app.get("/status")
def status():
    return {
        "core": "conectando",
        "detalle": "pendiente integración real"
    }
