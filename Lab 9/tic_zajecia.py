class Move:
  def __init__(self,x,y,sign):
    self.x = x
    self.y = y
    self.sign = sign

class Player:
  def __init__(self,name,sign):
    self.name = name
    self.sign = sign
  
  def get_move(self):
    print("Gracz: ",self.name)
    x,y = map(int, input().split())
    while x > 2 or x < 0 or y > 2 or y < 0:
      print("Niepoprawne dane!")
      x,y = map(int, input().split())
    return Move(x,y,self.sign)

class Board:
  def __init__(self):
    self.board = [["_","_","_"] for _ in range(3)]
    
  def __str__(self):
    return self.get_state()
    
  def get_state(self):
    state = ""
    for row in self.board:
      state += "".join(row) + "\n"
    return state
    
  def get_field(self, x, y):
    return self.board[x][y]
    
  def set_field(self,move):
    if self.get_field(move.x,move.y) != "_":
      print("Pole zajete!")
      return False
    self.board[move.x][move.y] = move.sign
    return True

class Game:
  def __init__(self):
    self.board = Board()
    self.winning_sign = None
  
  def play(self, player_one, player_two):
    players = (player_one, player_two)
    current_player = 0
    while not self.game_over():
      while not self.board.set_field(
        players[current_player].get_move()
      ):
        pass
      current_player = (current_player + 1) % 2
      print(self.board)
    if self.winning_sign is None:
      print("REMIS!")
    elif self.winning_sign == player_one.sign:
      print("Wygrał",player_one.name)
    else:
      print("Wygrał",player_two.name)
    
  def game_over(self):
    for row in range(3):
      if self.board.get_field(row,0) == \
      self.board.get_field(row,1) == \
      self.board.get_field(row,2) and \
      self.board.get_field(row,0) != "_":
        self.winning_sign = self.board.get_field(row,0)
        return True
    for column in range(3):
      if self.board.get_field(column,0) == \
      self.board.get_field(column,1) == \
      self.board.get_field(column,2) and \
      self.board.get_field(column,0) != "_":
        self.winning_sign = self.board.get_field(0,column)
        return True
          
    if self.board.get_field(0,0) == \
    self.board.get_field(1,1) == \
    self.board.get_field(2,2) and \
    self.board.get_field(0,0) != "_":
      self.winning_sign = self.board.get_field(0,0)
      return True
    
    if self.board.get_field(0,2) == \
    self.board.get_field(1,1) == \
    self.board.get_field(2,0) and \
    self.board.get_field(0,2) != "_":
      self.winning_sign = self.board.get_field(0,2)
      return True
      
    if not self.is_next_move_possible():
      return True
    
    return False
    
  def is_next_move_possible(self):
    for row in self.board.board:
      if '_' in row:
        return True
    return False

player_1 = Player("Marek","X")
player_2 = Player("Stefania","O")
game = Game()
game.play(player_1,player_2)