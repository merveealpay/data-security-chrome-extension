import os
import certifi

# Set the SSL_CERT_FILE environment variable to the certifi CA bundle
os.environ["SSL_CERT_FILE"] = certifi.where()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatgpt import check_sensitive_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataRequest(BaseModel):
    data: str

@app.post("/check-data")
async def check_data(request: DataRequest):
    result = await check_sensitive_data(request.data)
    if result:
        return {"warning": "You are sharing secret data. Please take care!"}
    return {"message": "Data is safe"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
