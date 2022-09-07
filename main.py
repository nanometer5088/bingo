def main():
    from src.init import inicio, idioma
    from src.cartelas import TUI_principal
    
    language = idioma()
    if language == "BR":
        x = 'src.constants.constants'
    elif language == "EN":
        x = 'src.constants.constantsen'

    import importlib
    locale = importlib.import_module(x)

    x = inicio(locale)
    if x == "instalado":
        print(locale.START["librariesinstalled"])
        return None
    TUI_principal(locale, language)
main()