from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Predictive Maintenance Copilot API",
    description="API untuk deteksi anomali, prediksi, dan agent chatbot.",
    version="0.1.0"
)


class StatusResponse(BaseModel):
    status: str
    message: str


@app.get("/", response_model=StatusResponse, tags=["Root"])
def read_root():
    return {
        "status": "ok", 
        "message": "Hello World - Predictive Maintenance BE Server is running!"
    }
