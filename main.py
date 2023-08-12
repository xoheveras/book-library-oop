from app.core.consoleApp import ConsoleApp
from colorama import init, Fore, Back, Style

if __name__ == "__main__":
    init(autoreset=True)
    app = ConsoleApp()
    app.run()