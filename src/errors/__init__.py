class MaxCardsPerPlayerReachedError(Exception):
    """
    Not enough cards to distribute amongst players.
    """
    pass


class MaxRoundsAchievedError(Exception):
    """
    Reached the max rounds in a game.
    """
    pass


class NotEnoughHandsError(Exception):
    """
    If there are not enough hands to take.
    """
    pass
