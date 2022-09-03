def main():
    from src.init import inicio
    from src.cartelas import TUI_principal
    x = inicio()
    if x == "instalado":
        print("Dependências instaladas com sucesso.\nAbra o programa novamente\n")
        return None
    TUI_principal()
main()