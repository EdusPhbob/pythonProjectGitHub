import random

print('Vamos jogar Jokenpô!')
itens = ('pedra','papel','tesoura')
jogador = int(input('(0) Pedra, (1)Papel ou (2) Tesoura, Qual a sua escolha ? '))
computador = random.randint(0,2)

if jogador > 2:
    print('BURRO é de 0 a 2 !')
else:
    print('Voce escolheu {}'.format(itens[jogador]),',Computador escolheu {} '.format(itens[computador]))
if jogador == computador:
    print('empate')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('vencedor')
else:
    print('perdedor')