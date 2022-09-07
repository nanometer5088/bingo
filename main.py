def main():
    import os
    from src.init import inicio, idioma
    from src.cartelas import TUI_principal
    #Lógica da seleção de idiomas - outras partes do programa dependem
    #das variáveis language e locale para apresentar o idioma correto
    language = ""
    while language == "":
        language = idioma()
        if language == "BR":
            x = 'src.constants.constants'
        elif language == "EN":
            x = 'src.constants.constantsen'
        elif language == "":
            os.system("cls || clear")
            input("Valor de entrada inválido\nPressione ENTER para continuar\n\nInvalid input value\nPress ENTER to continue")
    import importlib
    locale = importlib.import_module(x)
    #Introdução, verifica / instala dependências
    #verifica/cria arquivo de configuração
    #comentado em mais detalhes em init()
    x = inicio(locale)
    if x == "instalado":
        print(locale.START["librariesinstalled"])
        return None
    #Inicia o jogo
    TUI_principal(locale, language)
main()