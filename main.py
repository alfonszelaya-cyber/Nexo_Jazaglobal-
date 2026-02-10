
from fastapi import FastAPI

app = FastAPI(title="ZYRA NEXO CORE")

@app.get("/")
def root():
    return {"system": "ZYRA_NEXO_CORE", "status": "running"}
