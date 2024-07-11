from src.player import Player


def create_new_players(names: list[str, ...]) -> list[Player, ...]:
    """
    Create X num of Player's.

    Args:
        names (list[str]): Names of players playing.

    Returns:
        list[Player]: Player's
    """
    players = []
    print(f"Creating {len(names)} players")
    
    for name in names:
        player = Player(name=name)
        players.append(player)

    return players
