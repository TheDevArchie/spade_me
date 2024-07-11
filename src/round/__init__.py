
from ..errors import NotEnoughHandsError


class Round:
    def __init__(self, round: int, players: list[str, ...]):
        self._round = round
        self.cards_per_hand = (round - 6) if round > 6 else (8 - round)
        self._players = {player: {'predicted': 0, 'actual': 0} for player in players}
        self._available_hands = (round - 6) if round > 6 else (8 - round)

    @property
    def available_hands(self):
        return self._available_hands

    @available_hands.setter
    def available_hands(self, hands_taking: int):
        if hands_taking > self.available_hands:
            raise NotEnoughHandsError(f'Trying to take more hands than available')
        self._available_hands -= hands_taking

    @property
    def players(self):
        return self._players

    def update_players_predictions(self, players: dict[str, int]):
        for name, prediction in players.items():
            self.update_hands_taking(player=name, hands=prediction, phase='predicted')

    def update_hands_taking(self, player_name: str, hands: int, phase: str):
        if phase == 'predicted':
            self.available_hands = hands
        self.players[player_name][phase] = hands

    def calculate_player_score(self, player: str):
        hands_predicted = self.players[player]['predicted']
        hands_actual = self.players[player]['actual']

        if hands_predicted == hands_actual:
            return 10 + self.cards_per_hand

        return hands_actual
        
