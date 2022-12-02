
class RockPaperScissorsGame:

    # constants representing the point totals and named appropriately
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3

    # Encryption strategies
    ASSUMED_ENCRYPTION = 4
    ELF_ENCRYPTION = 5

    # Designates point value and identity for each symbol for easy comparisons
    SYMBOL_DEF: dict = {
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS,
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS
    }

    # Determines which item beats which: winners are keys, and losers are values
    DOMINANCE_DEF: dict = {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER
    }

    # Expected outcome keys
    LOSE = 6
    DRAW = 7
    WIN = 8

    # This is the elf definition for the 2nd puzzle
    ELF_DEF: dict = {
        'X': LOSE,
        'Y': DRAW,
        'Z': WIN
    }

    def __init__(self, opponent_move_encrypted: str, player_move_encrypted: str, encyption_strategy: int) -> None:
        if (encyption_strategy != self.ELF_ENCRYPTION and encyption_strategy != self.ASSUMED_ENCRYPTION):
            raise Exception("Encryption strategy is incorrect")

        self.encryption_strategy = encyption_strategy
        self.opponent_move = self.decrypt_opponent_move(opponent_move_encrypted)
        self.player_move = self.decrypt_player_move(player_move_encrypted)
        self.outcome = self.calculate_outcome()

    def calculate_outcome(self):
        outcome = 0
        # Player gets points for either a tie or winning
        if (self.player_move == self.opponent_move):
            outcome += 3
        elif (self.DOMINANCE_DEF[self.player_move] == self.opponent_move):
                outcome += 6

        outcome += self.player_move # Player gets points based on their move

        return outcome

    def get_outcome(self) -> int:
        return self.outcome

    def decrypt_player_move(self, move_encrypted: int) -> int:
        if (self.encryption_strategy == self.ELF_ENCRYPTION):
            if (self.ELF_DEF[move_encrypted] == self.WIN):
                # For a win, look up the key that dominates the opponent move.
                keys = self.DOMINANCE_DEF.keys()
                for key in keys:
                    if self.DOMINANCE_DEF[key] == self.opponent_move:
                        return key
            elif (self.ELF_DEF[move_encrypted] == self.DRAW):
                # For a draw, simply return the same move as the opponent
                return self.opponent_move
            else:
                # For a loss, look up the value that the opponent move dominates
                return self.DOMINANCE_DEF[self.opponent_move]
        else: 
            # otherwise, the encryption strategy is ASSUMED_ENCRYPTION
            return self.SYMBOL_DEF[move_encrypted]

    def decrypt_opponent_move(self, move_encrypted: int) -> int:
        return self.SYMBOL_DEF[move_encrypted]

def get_games_from_input(input_file_url: str, encryption_strategy: int) -> list[RockPaperScissorsGame]:
    games: list[RockPaperScissorsGame] = []
    with open(input_file_url) as file:
        for line in file.readlines():
            if not line.isspace():
                tokens = line.split()
                games.append(RockPaperScissorsGame(tokens[0], tokens[1], encryption_strategy))
    return games

def day_two_puzzle_one(input_file_url: str) -> None:
    games = get_games_from_input(input_file_url, RockPaperScissorsGame.ASSUMED_ENCRYPTION)
    print(sum([game.get_outcome() for game in games]))

def day_two_puzzle_two(input_file_url: str) -> None:
    games = get_games_from_input(input_file_url, RockPaperScissorsGame.ELF_ENCRYPTION)
    print(sum([game.get_outcome() for game in games]))

if __name__ == "__main__":
    input_file_url: str = "../input/day_two_puzzle_one_input.txt"

    day_two_puzzle_one(input_file_url)
    day_two_puzzle_two(input_file_url)