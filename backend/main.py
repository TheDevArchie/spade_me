from fastapi import FastAPI, HTTPException

from .models import (PlayerModel,
                     GameModel,
                     ScoreModel)

app = FastAPI() # Add version, and summary/description

games = []
scores = []
players = []


# /games
@app.get('/games')
def retrieve_all_games():
    return games


@app.get('/games/{game_id}')
def retrieve_game(game_id: int):
    for game in games:
        print(game.game_id)
        if game.game_id == game_id:
            return game

    raise HTTPException(status_code=404, detail='game not found')


@app.post('/games')
def add_game(game: GameModel):
    games.append(game)
    return game


# /players
@app.get('/players')
def retrieve_all_players():
    return players


@app.get('/players/{player_id}')
def retrieve_player(player_id: int):
    pass


@app.post('/players')
def add_player(player: PlayerModel):
    players.append(player)
    return player


# /scores
@app.get('/scores')
def retrieve_all_scores():
    return scores


@app.get('/scores/{score_id}')
def retrieve_score(score_id: int):
    pass


@app.post('/scores')
def add_scores(score: ScoreModel):
    scores.append(score)
    return score
