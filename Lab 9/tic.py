import numpy as np

class Board(object):
  def __init__(self):
   self.grid = [['_' for _ in range(3)] for _ in range(3)]
  
  def __str__(self):
    rows = []
    rows.append("  0 1 2")
    i = 0
    for row in self.grid:
      row_str = ' '.join(cell for cell in row)
      row_str = str(i)+" "+row_str
      rows.append(row_str)
      i+=1
    return '\n'.join(rows)

  def get_state(self):
    print(self)

  def get_field(self, x, y):
    return self.grid[x][y]

  def set_field(self, move):
    self.grid[move.y][move.x] = move.sign

class Move(object):
  def __init__(self, x, y, sign):
    self.x = x
    self.y = y
    self.sign = sign

class Player(object):
  def __init__(self,name,sign):
    self.name = name
    self.sign = sign
  
  def get_move(self):
    str_dim = input("Input attack coordinates \'row col\': ")
    x = int(str_dim[2])
    y = int(str_dim[0])
    return Move(x,y,self.sign)

class Game(object):
  def __init__(self):
    self.board = Board()

  def play(self, player_one, player_two):
    self.p1 = player_one
    self.p2 = player_two
    current_player = player_one
    state = 2
    while(state == 2):
      print("\n"+"".join("-" for _ in range(10)))
      self.board.get_state()
      print(f"Player: {current_player.name}")
      move = current_player.get_move()
      self.board.set_field(move)
      current_player = player_two if current_player is not player_two else player_one
      state = self.game_over()

    return state

  def game_over(self):
    s1 = self.p1.sign
    s2 = self.p2.sign
    np_board = np.array(self.board.grid)
    # kolumny
    for i in range(3):
      row = np_board[:,i]
      if len(row[row == s1]) == 3:
        return 1
      elif len(row[row == s2]) == 3:
        return -1
      
    # wiersze
    for i in range(3):
      col = np_board[i,:]
      if len(col[col == s1]) == 3:
        return 1
      elif len(col[col == s2]) == 3:
        return -1
        
    # skos
    if np_board[0,0] == np_board[1,1] == np_board[2,2] and np_board[1,1] != '_':
      return 1 if np_board[0,0] == s1 else -1
    if np_board[0,2] == np_board[1,1] == np_board[2,0] and np_board[1,1] != '_':
      return 1 if np_board[0,0] == s1 else -1

    if not self.is_next_move_possible():
      return 0
    return 2
    
  def is_next_move_possible(self):
    np_board_flat = np.array(self.board.grid).flatten()
    return not len(np_board_flat[np_board_flat != '_']) == 9



player_one = Player("Player One", "O")
player_two = Player("Player Two", "X")
game = Game()
result = game.play(player_one, player_two)
if result == 1:
  print(f"{player_one.name} WINS!!!")
elif result == -1:
  print(f"{player_two.name} WINS!!!")
else:
  print("DRAW!!!")
