from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    TITLE = Fore.CYAN + Style.BRIGHT
    SUCCESS = Fore.GREEN + Style.BRIGHT
    INFO = Fore.BLUE + Style.BRIGHT
    WARNING = Fore.YELLOW + Style.BRIGHT
    ERROR = Fore.RED + Style.BRIGHT

    TCP = Fore.GREEN
    UDP = Fore.YELLOW
    ICMP = Fore.RED
    OTHER = Fore.WHITE