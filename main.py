from classes.jogodavelha import JogoDaVelha
          
jogo = JogoDaVelha()
ganhador = False
jogador1 = True
jogador2 = False

while ganhador == False:
  
  jogo.toString()
  posicao1 = int(input("Linha (0 a 2)?"))
  posicao2 = int(input("Coluna (0 a 2)?"))

  if jogador1 == True:
    if jogo.jogaX(posicao1,posicao2) == True:
      jogador1 = False
      jogador2 = True
    else:
      print('Preencha as posições disponíveis')
    
  else:
    if jogo.jogaO(posicao1,posicao2)  == True:
      jogador2 = False
      jogador1 = True
    else:
      print('Preencha as posições disponíveis')

  ganhador = jogo.verifica()

jogo.toString()
if ganhador == True:
  if jogador1 == False:
    print("O jogador 1 ganhou!")
  else:
    print("O jogador 2 ganhou!")
elif ganhador == -1:
    print("Ninguém ganhou!")
  


