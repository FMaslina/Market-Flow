from contextlib import asynccontextmanager

from aiohttp import ClientSession
from fastapi import FastAPI, Request

from services.gateway.app.middleware import CorrelationIDMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client_session = ClientSession()
    yield
    await app.state.client_session.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(CorrelationIDMiddleware)


@app.get("/")
async def root():
    return {"message": "Index page"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


def get_client_session(request: Request) -> ClientSession:
    return request.app.state.client_session
