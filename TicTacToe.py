import random


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.won = 0
        self.lost = 0
        self.tied = 0
        self.played = 0
        self.isComputer = False

    def print_stats(self):
        print(self.name + " Stats:")
        print(
            "Played: %i, Won: %i, Lost: %i, Tied: %i"
            % (self.played, self.won, self.lost, self.tied)
        )
        print("-----------")

    def update_stats(self, won, tied):
        self.played += 1
        if tied:
            self.tied += 1
        else:
            if won:
                self.won += 1
            else:
                self.lost += 1


class Board:

    def __init__(self):
        # Initializes a empty grid
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1

    def display_board(self):
        col_num = 1
        print("    A   B   C")
        for row in self.grid:

            print("%i " % col_num, end="")
            for col in row:
                if col == 0:
                    print("|___", end="")
                else:
                    print("| " + col + " ", end="")

            print("|\n")
            col_num += 1

    def player_turn(self, square, val):
        if self.__is_valid_square(square):
            # Sets grid square to current player's symbol
            self.grid[int(square[1]) - 1][ord(square[0]) - 65] = val
            return True
        else:
            return False

    def has_won(self):
        return self.__row_match() or self.__col_match() or self.__diagonal_match()

    def has_tied(self):
        for row in self.grid:
            for col in row:
                if col == 0:
                    return False
        return True and not self.has_won()

    # Helper Function(s)

    def __row_match(self):
        for row in self.grid:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return True
        return False

    def __is_valid_square(self, square):
        return not (
            len(square) != 2
            or int(square[1]) > 3
            or ord(square[0]) < 65  # A
            or ord(square[0]) > 67  # C
            or self.grid[int(square[1]) - 1][ord(square[0]) - 65] != 0
        )

    def __col_match(self):
        # Transposes grid to make row matching easier
        t_grid = zip(*self.grid)
        for row in t_grid:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return True
        return False

    def __diagonal_match(self):
        return self.grid[1][1] != 0 and (
            self.grid[0][0] == self.grid[1][1] == self.grid[2][2]
            or self.grid[0][2] == self.grid[1][1] == self.grid[2][0]
        )


class Game:

    def __init__(self):
        self.board = Board()
        self.players = []

    def playRandomMove(self):
        available_moves = []

        for row in range(0, 3):
            for col in range(0, 3):
                square = chr(row + 65) + "%i" % (col + 1)
                if self.__is_valid_square(square):
                    available_moves.append(square)

        return random.choice(available_moves)

    def start_game(self):
        print("Hello, let's play Tic Tac Toe!\n")

        playWithComputer = False

        playWithComputerInput = input(
            "Would you like to play with a computer? (Y/N) ")

        if playWithComputerInput == "Y":
            playWithComputer = True

        # Adds players to the player list
        self.players.append(Player(input("Player 1 Name: "), "X"))

        if playWithComputer:
            self.players.append(Player("Computer", "O"))
        else:
            self.players.append(Player(input("Player 2 Name: "), "O"))

        print(
            "\nAlright, "
            + self.players[0].name
            + ", let's go! You will play with 'X's. "
        )

        self.play_game()

    def play_game(self):

        tie = False
        current_player = 0

        # Plays until one person wins
        while not self.board.has_won():

            if self.board.has_tied():
                tie = True
                break

            self.board.display_board()
            if self.players[current_player].name != "Computer":
                square = input(
                    self.players[current_player].name
                    + ", choose a square to play (e.g. A3): "
                )
            else:
                square = self.playRandomMove()
                print(square)

            # Plays the square if possible
            while not self.board.player_turn(
                square, self.players[current_player].symbol
            ):
                # Gets angry when user passes an invalid input
                square = input(
                    "Please choose an unfilled square between A1 and C3: ")

            current_player = self.switch_player(current_player)

        if tie:
            for player in self.players:
                player.update_stats(False, True)
        else:
            self.players[current_player].update_stats(False, False)
            # Switches player to display other's player's stats
            current_player = self.switch_player(current_player)
            self.players[current_player].update_stats(True, False)

        self.board.display_board()

        for player in self.players:
            # Displays the stats for both players
            player.print_stats()

        # Asks user whether he/she wants to play again
        play_again = input(self.play_again_prompt(tie, current_player))

        if play_again == "Y":
            self.board = Board()
            # Restarts game
            self.play_game()
        else:
            print("\nOk, play again some other time!")

    # Helper Function(s)

    def switch_player(self, current_player):
        # Switches from 0 to 1 and vice versa
        return 1 - current_player

    def play_again_prompt(self, tie, current_player):
        if not tie:
            if self.players[current_player].name != "Computer":
                return (
                    "Congratulations, "
                    + self.players[current_player].name
                    + ", you win! Would you like to play again? (Y/N) "
                )
            else:
                return "Sorry, the computer won this time. Play again? (Y/N) "
        return "It's a tie! Would you like to play again? (Y/N) "

    def __is_valid_square(self, square):
        return not (
            len(square) != 2
            or int(square[1]) > 3
            or ord(square[0]) < 65  # A
            or ord(square[0]) > 67  # C
            or self.board.grid[int(square[1]) - 1][ord(square[0]) - 65] != 0
        )


game = Game()
game.start_game()
