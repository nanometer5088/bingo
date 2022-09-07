START = {
    "intro": """
                    Project: Bingo Lite

            Algorithms and Programming II - Class 02D
                  Second semester - 2022


                  Press ENTER to continue
    """,
    "libraries": """
    
        The program detected that dependencies are not installed
             Press ENTER to install the necessary libraries

    (Note that you will need to open the program again after completion)
    """,
    "librariesinstalled": "Dependencies installed successfully.\nOpen the program again\n"}
INTRO = {
    "intro1": """
    At the beginning of the game, 4 cards will be drawn
      and the player will initially own the 1st card.

    ╔══════╦════╦════╦════╦════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║ 4  ║ 5  ║
    ╠══════╬════╬════╬════╬════╬════╣
    ║  ■   ║ 4  ║ 16 ║ 40 ║ 45 ║ 49 ║
    ║      ║ 4  ║ 17 ║ 25 ║ 38 ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ 43 ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║ 39 ║ 45 ║
    ╚══════╩════╩════╩════╩════╩════╝

    Press ENTER to continue
    """,
    "intro2": """
     If the player presses ENTER, a number is drawn and
       is marked on the cards in which it is present.

    ***************************************************
    **              Number drawn: 43                 **
    ***************************************************

    ╔══════╦════╦════╦════╦══════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬════╬════╬════╬══════╬════╣
    ║  ■   ║ 4  ║ 16 ║ 40 ║  45  ║ 49 ║
    ║      ║ 4  ║ 17 ║ 25 ║  38  ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ -43- ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║  39  ║ 45 ║
    ╚══════╩════╩════╩════╩══════╩════╝

    Press ENTER to continue
    """,
    "intro3": """
      If the player selects another card, he
     will become the owner of the chosen card.

    ***************************************************
    **              You now own card 2               **
    ***************************************************

    ╔══════╦════╦════╦════╦══════╦════╗
    ║ Dono ║ 1  ║ 2  ║ 3  ║  4   ║ 5  ║
    ╠══════╬════╬════╬════╬══════╬════╣
    ║      ║ 4  ║ 16 ║ 40 ║  45  ║ 49 ║
    ║  ■   ║ 4  ║ 17 ║ 25 ║  38  ║ 49 ║
    ║      ║ 12 ║ 22 ║ 31 ║ -43- ║ 47 ║
    ║      ║ 12 ║ 23 ║ 31 ║  39  ║ 45 ║
    ╚══════╩════╩════╩════╩══════╩════╝

    Press ENTER to continue
    """,
    "intro4": """
        If the card the player has is filled, the player wins.
    The program will ask for your name to be included in the list.
        The table is styled to represent the end of the game.

        The winner will be added to the vencedores.txt file,
               along with the match date and time.

    +------+------+------+------+------+------+
    | Dono |  1   |  2   |  3   |  4   |  5   |
    +------+------+------+------+------+------+
    |      | -4-  |  16  | -40- |  45  | -49- |
    |  ■   | -4-  | -17- | -25- | -38- | -49- |
    |      | -12- | -22- |  31  | -43- |  47  |
    |      | -12- |  23  |  31  |  39  |  45  |
    +------+------+------+------+------+------+    

    Congratulations! You won!!!
    Enter your name to appear on the list of winners:

    Press ENTER to continue
    """,
    "intro5": """
    If another card is filled, the game
      ends without the player winning.

    +------+------+------+------+------+------+
    | Dono |  1   |  2   |  3   |  4   |  5   |
    +------+------+------+------+------+------+
    |      | -4-  |  16  | -40- |  45  | -49- |
    |      | -4-  | -17- | -25- | -38- | -49- |
    |      | -12- | -22- |  31  | -43- |  47  |
    |  ■   | -12- |  23  |  31  |  39  |  45  |
    +------+------+------+------+------+------+  

    Another card has been completed!
    Better luck next time!

    Press ENTER to continue
    """,
    "introfinal": """
                   Ready?
            Press ENTER to play!

    The tutorial can be done again by removing
               the config.json file
    """}

SELECTED = {
    "player": "■",
    "notplayer": " "}

ERRORS = {
    "invalid": "Invalid input value",}

WARNING = {
    "firstime": """
        The program has detected that this is the first time it is playing.

                          Press ENTER to watch the tutorial.
    Alternatively, press 1 to skip the tutorial (Recommended for experienced players)
    """,
    "firsttimeskip": """
                 No problem, good game!

            The tutorial can be done by removing
                   the config.json file

                   Press ENTER to play!
            """}
GAME = {
    "presskey": "Select another card (1, 2, 3 or 4) or press ENTER to draw "}


SCOREBOARD = {
    "win": """
    Congratulations! You won!!!
    Enter your name to appear on the list of winners:
    """,
    "loss": """
     Another card has been completed!
          Better luck next time!
    """}