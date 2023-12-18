import asyncio

import uvicorn
from app import settings
from fastapi import FastAPI, APIRouter, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from utils import FILES, LABELED_BOARD, RANKS, SQUARE_TYPE
from utils.game import Game
from utils.move import Move
from utils.piece import Color

app = FastAPI()

URL = settings.WEBSITE_URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=[URL],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
) # type: ignore

web_router = APIRouter(default_response_class=Response)

app.host(URL, web_router)


def main():
    game_state = Game()

    # Board Configuration
    board = game_state.board
    board.setup()

    # Game loop
    while game_state.winner is None:
        whos_turn = (
            Color.WHITE if game_state.current_turn == Color.WHITE else Color.BLACK
        )

        selected_sqr = input("Select Piece: ").upper()
        new_sqr = input("Select Destination: ")
        if not len(selected_sqr) == 2:
            continue

        if not selected_sqr[0] in FILES or not selected_sqr[1] in RANKS:
            continue

        game_state.players[whos_turn]


if "__main__" == __name__:
    uvicorn.run(app=app, port=settings.PORT)
