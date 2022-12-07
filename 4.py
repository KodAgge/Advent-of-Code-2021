import numpy as np

class Board():

    def __init__(self, board, id) -> None:
        self.board = np.array(board)
        self.id = id
        self.drawn = np.zeros(self.board.shape)
        self.has_won = False

    def __repr__(self) -> str:
        return str(self.board)

    def draw_number(self, number):
        self.drawn += self.board == number
        
    def check_win(self):
        return np.any(np.sum(self.drawn, axis = 0) == 5) or np.any(np.sum(self.drawn, axis = 1) == 5)

    def get_score(self, draw):
        return int(draw * np.sum((1 - self.drawn) * self.board))

def read_file(file_name = "4.in"):
    with open(file_name) as file:
        boards = []
        j = 0
        for i, line in enumerate(file):
            if i == 0:
                draws = list(map(int, line.strip().split(",")))
            else:
                if line == "\n":
                    board_list = []
                else:
                    board_list.append([int(line[i:i+2].strip()) for i in range(0,len(line.rstrip()),3)])
                    if len(board_list) == 5:
                        j += 1
                        boards.append(Board(board_list, j))
    return boards, draws

# Part 1

boards, draws = read_file()
game_over = False
for draw in draws:
    for board in boards:
        board.draw_number(draw)
        game_over = board.check_win()
        if game_over:
            print(f"Answer part 1: {board.get_score(draw)}")
            break
    if game_over:
        break


# Part 2
boards, draws = read_file()
won_boards = [0 for _ in range(len(boards))]
for draw in draws:
    for board in boards:
        board.draw_number(draw)
        if board.check_win():
            won_boards[board.id - 1] = 1
            if sum(won_boards) == len(won_boards):
                print(f"Answer part 2: {board.get_score(draw)}")
                break
    if sum(won_boards) == len(won_boards):
        break