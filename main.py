def main():
    from src.init import inicio
    from src.cartelas import TUI_principal
    from src.constants import START
    x = inicio()
    if x == "instalado":
        print(START["librariesinstalled"])
        return None
    TUI_principal()
main()