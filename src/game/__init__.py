from ..errors import (MaxCardsPerPlayerReachedError,
                      MaxRoundsAchievedError)
from ..player import Player
from ..round import Round


class Game:
    def __init__(self, starting_cards_dealt: int, players: list[Player]):
        if starting_cards_dealt * len(players) > 52:
            raise MaxCardsPerPlayerReachedError('Not Enough Cards to distribute evenly!')
        self.NUM_OF_ROUNDS: int = (starting_cards_dealt * 2) - 1
        self._current_round: int = 1
        self._rounds: dict[Round] = {}
        self._players: list[Player] = players

    @property
    def current_round_num(self):
        return self._current_round

    @current_round_num.setter
    def current_round_num(self, next_round):
        self.current_round_num = next_round

    @property
    def round(self) -> Round:
        return self._round[current_round_num]

    def setup_next_round(self):
        if self.NUM_OF_ROUNDS > self.current_round:
            raise MaxRoundsAchievedError("Reached end of game")
        self.current_round = self.current_round + 1
        next_round = Round(round=self.current_round, players=self._players)
        self._rounds[self.current_round] = next_round

    def start_round(self):
        """
        Filling in players predictions.
        """
        predictions = {}
        for player in self.players:
            prediction = 0 # TODO: MODIFY TO ACTUAL CALL
            predictions[player.name] = prediction

        self.round.update_players_predictions(predictions=players_predictions, phase='predicted')

    def finish_round(self):
        """
        Filling in players actual.
        """
        actuals = {}
        for player in self.players:
            actual = 0 # TODO: MODIFY TO ACTUAL CALL
            actuals[player.name] = actual

        self

    def finish_game(self):
        """
        Calculate all players total scores, determine winner.
        """
        pass
