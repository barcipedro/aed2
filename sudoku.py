 def is_valid(board, row, col, num):
    # Verifica se o número num já existe na linha
    for i in range(9):
        if board[row][i] == num:
            return False

    # Verifica se o número num já existe na coluna
    for i in range(9):
        if board[i][col] == num:
            return False

    # Verifica se o número num já existe no bloco 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            # Encontra uma célula vazia
            if board[row][col] == 0:
                # Tenta preencher a célula com os números de 1 a 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # Se for válido, preenche a célula com o número num
                        board[row][col] = num

                        # Chama recursivamente a função para preencher as células restantes
                        if solve_sudoku(board):
                            return True

                        # Se a recursão não encontrar uma solução válida, desfaz a atribuição
                        board[row][col] = 0

                # Se nenhum número for válido, retorna False para desfazer a atribuição anterior
                return False

    # Se todas as células estiverem preenchidas, retorna True para indicar que a solução foi encontrada
    return True

# Configuração inicial do Sudoku
board = [
    [0, 0, 6, 0, 9, 0, 0, 4, 0],
    [0, 0, 0, 3, 7, 1, 0, 0, 8],
    [0, 3, 0, 0, 0, 0, 9, 0, 7],
    [4, 0, 0, 5, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 7, 0, 0, 5],
    [2, 0, 8, 0, 0, 0, 0, 3, 0],
    [5, 0, 0, 7, 3, 8, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 5, 0, 0]
]

if solve_sudoku(board):
    # Imprime a solução encontrada
    for row in board:
        print(row)
else:
    print("Não foi possível encontrar uma solução para o Sudoku.")
