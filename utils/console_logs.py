import colorama

def colorInfo(text: str):
    print(colorama.Fore.GREEN + "[INFO] " + colorama.Fore.RESET + text)
def colorError(text: str):
    print(colorama.Fore.RED + "[ERR] " + colorama.Fore.RESET + text)
