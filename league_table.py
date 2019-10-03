"""
The LeagueTable class tracks the score of each player in a league.
After each game, the player records their score with the record_result function.
The player's rank in the league is calculated using the following logic:
 * The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
 * If two players are tied on score, then the player who has played the fewest games is ranked higher.
 * If two players are tied on score and number of games played,
   then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.

For example:
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))

All players have the same score. 
However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players,
 he is ranked first. Therefore, the code above should display "Chris".
"""


class LeagueTable:
    __empty_player = {'scores': 0, 'games': 0, 'last_game': None}
    __last_game = 0

    def __init__(self, players: list):
        self.players = {p: dict(LeagueTable.__empty_player) for p in players}  # dict() need to make a new objs

    def __srt__(self):
        return f'<LeagueTable obj: {self.players}>'

    def record_result(self, player: str, score: int):
        data_player = self.players.get(player)
        if data_player:
            data_player['scores'] += score
            data_player['games'] += 1
            data_player['last_game'] = self.__get_last_game()

    def player_rank(self, rank=None):
        if rank and (rank > len(self.players) or rank < 0):
            return None
        ps = self.players

        # List of Tuples [(player name, scores, games, game order) ... ]
        table_rank = [(p, ps[p]['scores'], ps[p]['games'], ps[p]['last_game']) for p in ps]
        table_rank = sorted(table_rank, key=lambda p: (-p[1], p[2], p[3]))

        if rank:
            return table_rank[rank - 1]
        return table_rank

    def add_player(self):
        pass

    @classmethod
    def __get_last_game(cls, ):
        cls.__last_game += 1
        return cls.__last_game


if __name__ == '__main__':
    table = LeagueTable(['Mike', 'Chris', 'Arnold', 'Nike', 'Max'])
    table.record_result('Max', 2)
    table.record_result('Nike', 2)
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print('The leader:', table.player_rank(1), )

    from pprint import pprint

    print("\nRating of all players")
    pprint(table.player_rank())

    print("\nPlayers")
    pprint(table.players)
