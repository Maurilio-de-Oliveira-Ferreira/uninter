                                    # JOGO DA VELHA (TIC-TAC-TOE)

'''O computador joga com 'X' e sempre começa no centro do tabuleiro.
   O usuário joga com 'O', digitando o número (1 a 9) do quadrado escolhido.
   O computador escolhe suas jogadas de forma aleatória.
'''

from random import randrange


def display_board(board):
    # Exibe o tabuleiro no console, exatamente no formato do exemplo.
    linha = '+-------+-------+-------+'
    vazio = '|       |       |       |'
    print(linha)
    for row in range(3):
        print(vazio)
        print('|   ' + '   |   '.join(str(board[row][col]) for col in range(3)) + '   |')
        print(vazio)
        print(linha)


def enter_move(board):
    # Pede o movimento do usuário, valida e atualiza o tabuleiro.
    livres = make_list_of_free_fields(board)
    while True:
        entrada = input('Digite seu movimento: ')
        try:
            movimento = int(entrada)
        except ValueError:
            print('Entrada inválida! Digite um número inteiro de 1 a 9.')
            continue
        if movimento <= 0 or movimento >= 10:
            print('Número inválido! Digite um número de 1 a 9.')
            continue
        row = (movimento - 1) // 3
        col = (movimento - 1) % 3
        if (row, col) not in livres:
            print('Esse quadrado já está ocupado! Escolha outro.')
            continue
        board[row][col] = 'O'
        return


def make_list_of_free_fields(board):
    # Retorna a lista de tuplas (linha, coluna) dos quadrados livres.
    livres = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('O', 'X'):
                livres.append((row, col))
    return livres


def victory_for(board, sign):
    # Verifica se o jogador que usa 'sign' ('O' ou 'X') venceu.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:  # linhas
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:  # colunas
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:      # diagonal principal
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:      # diagonal secundária
        return True
    return False


def draw_move(board):
    # O computador escolhe aleatoriamente um quadrado livre e coloca um 'X'.
    livres = make_list_of_free_fields(board)
    if len(livres) > 0:
        row, col = livres[randrange(len(livres))]
        board[row][col] = 'X'


def main():
    # Tabuleiro 3x3: cada quadrado livre guarda seu número; acesso por board[row][column].
    board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]
    board[1][1] = 'X'  # o primeiro movimento do computador é sempre no centro
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print('Você ganhou!')
            break
        if len(make_list_of_free_fields(board)) == 0:
            print('Empate!')
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print('Eu ganhei!')
            break
        if len(make_list_of_free_fields(board)) == 0:
            print('Empate!')
            break


if __name__ == '__main__':
    main()
