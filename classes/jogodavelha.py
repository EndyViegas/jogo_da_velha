class JogoDaVelha():

    def __init__(self):
          self._coordernadas = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
         

    def jogaO(self, x, y):
          if self._coordernadas[x][y] == ' ':
              self._coordernadas[x][y] = 'O'
              return True
          else:
              return False
    def jogaX(self, x, y):
          if self._coordernadas[x][y] == ' ':
              self._coordernadas[x][y] = 'X'
              return True
          else:
            return False


    def verifica(self):
          if self._coordernadas[0][0] == self._coordernadas[1][0] and self._coordernadas[1][0] == self._coordernadas[2][0] and self._coordernadas[0][0] != ' ' and self._coordernadas[1][0] != ' ' and self._coordernadas[2][0] != ' ':
              return True
          elif self._coordernadas[0][0] == self._coordernadas[0][1] and self._coordernadas[0][1] == self._coordernadas[0][2] and self._coordernadas[0][0] != ' ' and self._coordernadas[0][1] != ' ' and self._coordernadas[0][2] != ' ':
              return True
          elif self._coordernadas[0][1] == self._coordernadas[1][1] and self._coordernadas[1][1] == self._coordernadas[2][1] and self._coordernadas[0][1] != ' ' and self._coordernadas[1][1] != ' ' and self._coordernadas[2][1] != ' ':
              return True
          elif self._coordernadas[0][2] == self._coordernadas[1][2] and self._coordernadas[1][2] == self._coordernadas[2][2] and self._coordernadas[0][2] != ' ' and self._coordernadas[1][2] != ' ' and self._coordernadas[2][2] != ' ':
              return True
          elif self._coordernadas[1][0] == self._coordernadas[1][1] and self._coordernadas[1][1] == self._coordernadas[1][2] and self._coordernadas[1][0] != ' ' and self._coordernadas[1][1] != ' ' and self._coordernadas[1][2] != ' ':
              return True
          elif self._coordernadas[2][0] == self._coordernadas[2][1] and self._coordernadas[2][1] == self._coordernadas[2][2] and self._coordernadas[2][0] != ' ' and self._coordernadas[2][1] != ' ' and self._coordernadas[2][2] != ' ':
              return True
          elif self._coordernadas[0][0] == self._coordernadas[1][1] and self._coordernadas[1][1] == self._coordernadas[2][2] and self._coordernadas[0][0] != ' ' and self._coordernadas[1][1] != ' ' and self._coordernadas[2][2] != ' ':
              return True
          elif self._coordernadas[0][2] == self._coordernadas[1][1] and self._coordernadas[1][1] == self._coordernadas[2][0] and self._coordernadas[0][2] != ' ' and self._coordernadas[1][1] != ' ' and self._coordernadas[2][0] != ' ':
              return True
          elif self._coordernadas[0][0] != " " and self._coordernadas[0][1] != " " and self._coordernadas[0][2] != " " and self._coordernadas[1][0] != " " and self._coordernadas[1][1] != " " and self._coordernadas[1][2] != " " and self._coordernadas[2][0] != " " and self._coordernadas[2][1] != " " and self._coordernadas[2][2] != " ":
              return -1
          else:
              return False


    def toString(self):
          print('   0    1   2')
          print('')
          print('0   '+self._coordernadas[0][0]+' | '+self._coordernadas[0][1]+' | '+self._coordernadas[0][2])
          print('1   '+self._coordernadas[1][0]+' | '+self._coordernadas[1][1]+' | '+self._coordernadas[1][2])
          print('2   '+self._coordernadas[2][0]+' | '+self._coordernadas[2][1]+' | '+self._coordernadas[2][2])