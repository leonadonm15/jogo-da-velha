tabuleiro = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']


def mostrar_tabuleiro():  # mostra o tabuleiro
    print(f'{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')


def jogada():  # recebe o input da jogada feita pelo jogador
    x = int(input('De 1 a 9, qual a jogada que voce quer fazer ? '))
    x -= 1
    return x


def fazer_jogada(x, y):
    '''
    :param x: lugar onde quer marcar
    :param y: jogador x ou o
    :return: se jogada for invalida retona False
    '''
    if tabuleiro[x] == '-':
        tabuleiro[x] = y
    else:
        print('JOGADA INVALIDA')
        return False


def troca_de_jogador(n):  # verifica se é a vez do X ou do O vendo se o numero da jogada é par ou impar
    if n % 2 == 0:
        return 'O'
    else:
        return 'X'


def vencedor():  # lista todas as possíveis vitórias e itera pelo tabuleiro buscando uma
    '''
    linhas vitoriosas:
        horizontais: 1, 2, 3 | 4, 5, 6 | 7, 8, 9
        veticais: 1, 4, 7 | 2, 5, 8 | 3, 6, 9
        cruzadas: 1, 5, 9 | 3, 5, 7
    '''
    vitoria = [(tabuleiro[0], tabuleiro[1], tabuleiro[2]),  # vitorias horizontais
               (tabuleiro[3], tabuleiro[4], tabuleiro[5]),
               (tabuleiro[6], tabuleiro[7], tabuleiro[8]),

               (tabuleiro[0], tabuleiro[3], tabuleiro[8]),  # vitorias verticais
               (tabuleiro[1], tabuleiro[4], tabuleiro[7]),
               (tabuleiro[2], tabuleiro[5], tabuleiro[8]),

               (tabuleiro[0], tabuleiro[4], tabuleiro[8]),  # vitorias cruzadas
               (tabuleiro[2], tabuleiro[4], tabuleiro[8])]

    for tupla in vitoria:
        Xcontador = 0
        Ocontador = 0
        for iten in tupla:
            if iten != '-':  # iterar pela lista de tuplas vitorioas, se uma das combinações marcar 3 no score de pontuação o jogo acaba
                if iten == 'X':
                    Xcontador += 1
                    if Xcontador == 3:
                        return True
                if iten == 'O':
                    Ocontador += 1
                    if Ocontador == 3:
                        return True


'''
loop infinito que representa as rodadas do jogo e a ordem e condições as quais as funções sao executadas
'''
n = 0
jogando = True
while jogando is True:
    mostrar_tabuleiro()
    if fazer_jogada(jogada(), troca_de_jogador(n)) is False:
        jogando = True
        n -= 1
    if vencedor() is True:
        mostrar_tabuleiro()
        print('Voce venceu')
        break
    n += 1
    if n == 9:
        print('DEU VELHA')
        mostrar_tabuleiro()
        break
