from fastapi import FastAPI

from services.gateway.app.middleware import CorrelationIDMiddleware

app = FastAPI()

app.add_middleware(CorrelationIDMiddleware)


@app.get("/")
async def root():
    return {"message": "Index page"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
