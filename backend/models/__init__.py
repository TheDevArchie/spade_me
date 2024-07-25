from pydantic import BaseModel


class PlayerModel(BaseModel):
    player_id: int
    name: str


class GameModel(BaseModel):
    game_id: int
    winner_id: int
    num_of_rounds: int


class ScoreModel(BaseModel):
    score_id: int
    player_id: int
    game_id: int
    score: int
