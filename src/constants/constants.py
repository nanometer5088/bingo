START = {
    "intro": """
                    Projeto: Bingo Lite
                    
            Algoritmos e Programação II - Turma 02D
                  Segundo semestre - 2022


                Pressione ENTER para continuar
    """,
    "libraries": """
    
        O programa detectou que as dependências não estão instaladas
        Pressione ENTER para instalar as bibliotecas necessárias

    (Note que será necessário abrir o programa novamente após a conclusão)
    """,
    "librariesinstalled": "Dependências instaladas com sucesso.\nAbra o programa novamente\n"}
INTRO = {
    "intro1": """
     No início do jogo, serão sorteadas 4 cartelas
    e o jogador será dono inicialmente da 1ª cartela.

    ╔══════╦════╦════╦════╦════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║ 4  ║ 5  ║
    ╠══════╬════╬════╬════╬════╬════╣
    ║  ■   ║ 4  ║ 16 ║ 40 ║ 45 ║ 49 ║
    ║      ║ 4  ║ 17 ║ 25 ║ 38 ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ 43 ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║ 39 ║ 45 ║
    ╚══════╩════╩════╩════╩════╩════╝

    Pressione ENTER para continuar
    """,
    "intro2": """
    Se o jogador pressionar ENTER, um número é sorteado e
       é marcado nas cartelas em que estiver presente.

    ***************************************************
    **         Número Sorteado: 43                   **
    ***************************************************

    ╔══════╦════╦════╦════╦══════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬════╬════╬════╬══════╬════╣
    ║  ■   ║ 4  ║ 16 ║ 40 ║  45  ║ 49 ║
    ║      ║ 4  ║ 17 ║ 25 ║  38  ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ -43- ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║  39  ║ 45 ║
    ╚══════╩════╩════╩════╩══════╩════╝

    Pressione ENTER para continuar
    """,
    "intro3": """
    Se o jogador selecionar outra cartela, ele
     passará a ser dono da cartela escolhida.

    ***************************************************
    **         Você agora é dono da cartela 2        **
    ***************************************************

    ╔══════╦════╦════╦════╦══════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬════╬════╬════╬══════╬════╣
    ║      ║ 4  ║ 16 ║ 40 ║  45  ║ 49 ║
    ║  ■   ║ 4  ║ 17 ║ 25 ║  38  ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ -43- ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║  39  ║ 45 ║
    ╚══════╩════╩════╩════╩══════╩════╝

    Pressione ENTER para continuar
    """,
    "intro4": """
    Se a cartela que o jogador possui for preenchida, ele vence.
       O programa solicitará seu nome para constar no rol.
  A tabela tem seu estilo alterado para representar o final do jogo.
    
    O vencedor será adicionado ao arquivo vencedores.txt,
            junto da data e horário da partida.

    +------+------+------+------+------+------+
    | Dono |  1   |  2   |  3   |  4   |  5   |
    +------+------+------+------+------+------+
    |      | -4-  |  16  | -40- |  45  | -49- |
    |  ■   | -4-  | -17- | -25- | -38- | -49- |
    |      | -12- | -22- |  31  | -43- |  47  |
    |      | -12- |  23  |  31  |  39  |  45  |
    +------+------+------+------+------+------+    

    Parabéns! Você venceu!!!
    Entre o seu nome para constar no rol de vencedores:

    Pressione ENTER para continuar
    """,
    "intro5": """
    Se outra cartela for preenchida, a partida
        termina sem a vitória do jogador.

    +------+------+------+------+------+------+
    | Dono |  1   |  2   |  3   |  4   |  5   |
    +------+------+------+------+------+------+
    |      | -4-  |  16  | -40- |  45  | -49- |
    |      | -4-  | -17- | -25- | -38- | -49- |
    |      | -12- | -22- |  31  | -43- |  47  |
    |  ■   | -12- |  23  |  31  |  39  |  45  |
    +------+------+------+------+------+------+  

    Outra cartela foi completada!
    Melhor sorte da próxima vez!

    Pressione ENTER para continuar
    """,
    "introfinal": """
                    Preparado?
            Pressione ENTER para jogar!
            
    O tutorial pode ser feito novamente removendo
               o arquivo config.json
    """}

SELECTED = {
    "player": "■",
    "notplayer": " "}

ERRORS = {
    "invalid": "Valor de entrada inválido. Possíveis valores são: ",}

WARNING = {
    "firstime": """
                O programa detectou que esta é a primeira vez que está jogando.
    
                          Pressione ENTER para assistir o tutorial.
    Alternativamente, pressione 1 para pular o tutorial (Recomendado para jogadores experientes)
    """,
    "firsttimeskip": """
                  Sem problemas, bom jogo!

            O tutorial pode ser feito removendo
                   o arquivo config.json

                 Pressione ENTER para jogar!
            """}
GAME = {
    "presskey": "Selecione outra cartela (1, 2, 3 ou 4) ou pressione ENTER para sortear "}


SCOREBOARD = {
    "win": """
    Parabéns! Você venceu!!!
    Entre o seu nome para constar no rol de vencedores:
    """,
    "loss": """
    Outra cartela foi completada!
    Melhor sorte da próxima vez!
    """}