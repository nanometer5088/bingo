START = {
    "intro": """
                    Projeto: Bingo Lite
            Algoritmos e Programação II - Turma 02D
                  Segundo semestre - 2022


    Certifique-se que tenha as bibliotecas necessárias instaladas

    Pressione ENTER para instalar as bibliotecas necessárias

    As bibliotecas podem ser instaladas posteriormente rodando o
                        arquivo 'setup.py'
    """,
    "intro1": """
     No início do jogo, serão sorteadas 4 cartelas
    e o jogador será dono inicialmente da 1ª cartela.

    ***************************************************
    **         Você agora é dono da cartela 1        **
    ***************************************************

    ╔══════╦═══╦════╦════╦════╦════╗
    ║ Dono ║ 1 ║ 2  ║ 3  ║ 4  ║ 5  ║
    ╠══════╬═══╬════╬════╬════╬════╣
    ║  ■   ║ 6 ║ 12 ║ 20 ║ 27 ║ 29 ║
    ║      ║ 7 ║ 19 ║ 28 ║ 42 ║ 46 ║
    ║      ║ 7 ║ 17 ║ 19 ║ 33 ║ 37 ║
    ║      ║ 5 ║ 17 ║ 19 ║ 26 ║ 46 ║
    ╚══════╩═══╩════╩════╩════╩════╝

    Pressione ENTER para continuar
    """,
    "intro2": """
    Se o jogador pressionar ENTER, um número é sorteado e
       é marcado nas cartelas em que estiver presente.

    ***************************************************
    **         Número Sorteado: 33                   **
    ***************************************************

    ╔══════╦═══╦════╦════╦══════╦════╗
    ║ Dono ║ 1 ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬═══╬════╬════╬══════╬════╣
    ║  ■   ║ 6 ║ 12 ║ 20 ║  27  ║ 29 ║
    ║      ║ 7 ║ 19 ║ 28 ║  42  ║ 46 ║
    ║      ║ 7 ║ 17 ║ 19 ║ [33] ║ 37 ║
    ║      ║ 5 ║ 17 ║ 19 ║  26  ║ 46 ║
    ╚══════╩═══╩════╩════╩══════╩════╝

    Pressione ENTER para continuar
    """,
    "intro3": """
    Se o jogador selecionar outra cartela, ele
     passará a ser dono da cartela escolhida.


    ***************************************************
    **         Você agora é dono da cartela 2        **
    ***************************************************

    ╔══════╦═══╦════╦════╦══════╦════╗
    ║ Dono ║ 1 ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬═══╬════╬════╬══════╬════╣
    ║      ║ 6 ║ 12 ║ 20 ║  27  ║ 29 ║
    ║  ■   ║ 7 ║ 19 ║ 28 ║  42  ║ 46 ║
    ║      ║ 7 ║ 17 ║ 19 ║ [33] ║ 37 ║
    ║      ║ 5 ║ 17 ║ 19 ║  26  ║ 46 ║
    ╚══════╩═══╩════╩════╩══════╩════╝


    Pressione ENTER para continuar
    """
    }

SELECTED = {
    "player": "■",
    "notplayer": " "
    }
ERRORS = {
    "invalid": "Valor de entrada inválido",
}
WARNING = {
    "firstime": """
                O programa detectou que esta é a primeira vez que está jogando.
    
                          Pressione ENTER para assistir o tutorial.
    Alternativamente, pressione 1 para pular o tutorial (Recomendado para jogadores experientes)
    """
}
SCOREBOARD = {
    "win": """
    Parabéns! Você venceu!!!
    Entre o seu nome para constar no rol de vencedores:
    """}
