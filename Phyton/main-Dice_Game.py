from random import randint
#Essa ação é feita para importar da biblioteca um número aleatório.
bouts = 1
#Aqui definiremos o número de rodadas(bouts) = 1, visto que todo jogo começa na primeira rodada.
plus = 0
#Esse será o somatório dos dados/pontos obtidos pelo jogador.
while bouts <= 4:
#Aqui colocaremos uma estrutura de laço(loop), indicando que as ações dentro dela irão se repetir enquanto o número de rodadas for menor ou igual a quatro.
  dice_number = randint(1,6)
#Nesse caso indicaremos que o número que o dado "rolar" estará no intervalo de 1 até 6, mostrando as faces dele.
  user_choice = int(input("Digite uma opção: 1 - Rolar o dado ou 2 - Finalizar rodada: "))
#Já aqui nós iremos fazer o usuário escolher entre duas opções por meio da digitação, no intuito de que ele fique "rolando" o dado ou encerre sua rodada e preserve seus pontos.
  if user_choice == 1:
    print("O número que saiu do dado foi: {}".format(dice_number))
#Nessa conjuntura usaremos estrutura if para, caso o usuário tenha digitado 1(Continuar rolando), imprimir o número do dado, mostrando ao usuário seu resultado.
    if dice_number == 3:
      print("Você perdeu todos os seus pontos")
      plus = 0 
      bouts = bouts + 1
#Se esse número for = 3, o contador de pontos irá se tornar 0 e será imprimido que a pessoa perdeu todos os seus pontos. Além disso, o número de rodadas aumentará em 1, representando o fim da rodada e início da próxima.
    elif dice_number == 6:
      print("Seus pontos serão duplicados!")
      plus = plus * 2
#Se o número do dado for = 6, os pontos serão duplicados no contador de pontos e será imprimida essa mensagem.
    else:
     print("Você terá esses pontos adicionados.")
     plus = plus + dice_number
#Caso o usuário tenha tirado os números [1,2,4,5], eles serão adicionados no contador de pontos e será imprimida essa mensagem.      
    print("Essa é a sua pontuação atual: {}".format(plus))
#No final de cada rolada de dado, a pontuação atual será exibida, comprovando ao usuário que dobrou, a adição dos pontos ou sua perda total.  
  elif user_choice == 2:
    bouts = bouts + 1 
#A estrutura elif é utilizada caso o jogador escolha a opção dois, que implicará na conservação dos pontos e fim da rodada.
print("Sua pontuação total foi: {}".format(plus))
#Por fim, será imprimida a pontuação total do usuário. É isso, espero que tenha gostado da explicação! ^-^