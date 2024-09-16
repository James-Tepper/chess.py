import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from routers.account_routes import router as account_router
from routers.auth_routes import router as auth_router
from routers.game_routes import router as game_router
from routers.move_routes import router as move_router
from routers.player_routes import router as player_router

from app import lifecycle, settings

WEB_URL = settings.WEBSITE_URL
HOSTING = f"api.{WEB_URL}" if not WEB_URL == "local" else "localhost"

app = FastAPI()

# app.include_router(player_router, prefix="/players")
app.include_router(account_router, prefix="/accounts")
app.include_router(player_router, prefix="/players")
app.include_router(auth_router, prefix="/auth")
app.include_router(game_router, prefix="/games")
app.include_router(move_router, prefix="/moves")


app.add_middleware(
    CORSMiddleware,
    allow_origins=WEB_URL,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.on_event("startup")
async def startup() -> None:
    await lifecycle.start()


@app.on_event("shutdown")
async def shutdown() -> None:
    await lifecycle.shutdown()


if __name__ == "__main__":
    uvicorn.run(app=app, host=HOSTING, port=settings.PORT)
