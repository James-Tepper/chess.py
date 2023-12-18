import uvicorn
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from utils import FILES, LABELED_BOARD, RANKS, SQUARE_TYPE
from utils.game import Game
from utils.piece import Color
from utils.board import ChessBoard
from app import lifecycle, settings

app = FastAPI()

WEB_URL = settings.WEBSITE_URL

# Routers
api_router = APIRouter()
web_router = APIRouter(default_response_class=Response)

# Web Host
app.host(WEB_URL, web_router)

# API Parameters
HOSTING = f"api.{WEB_URL}" if not WEB_URL == "local" else "localhost"

# API Host
app.host(HOSTING, api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[WEB_URL],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)  # type: ignore


@app.on_event("startup")
async def startup() -> None:
    await lifecycle.start()


@app.on_event("shutdown")
async def shutdown() -> None:
    await lifecycle.shutdown()


def main():
    _board = ChessBoard()
    game_state = Game(_board)

    # Board Configuration

    game_state.board.setup()

    # Game loop
    # while game_state.winner is None:
    #     whos_turn = (
    #         Color.WHITE if game_state.current_turn == Color.WHITE else Color.BLACK
    #     )

    #     selected_sqr = input("Select Piece: ").upper()
    #     new_sqr = input("Select Destination: ")
    #     if not len(selected_sqr) == 2:
    #         continue

    #     if not selected_sqr[0] in FILES or not selected_sqr[1] in RANKS:
    #         continue

    #     game_state.players[whos_turn]


if "__main__" == __name__:
    main()
    uvicorn.run(app=app, port=settings.PORT)
