import time
import sys


class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'


def type_print(text, delay=0.02):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_menu():
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════════╗")
    print(
        f"║          {Colors.BOLD}🚀 Mini-OS Command Menu{Colors.CYAN}           ║")
    print(f"╠════════════════════════════════════════════╣")
    print(
        f"║ {Colors.GREEN}ls{Colors.CYAN}      : List files and directories     📁 ║")
    print(
        f"║ {Colors.GREEN}cd{Colors.CYAN}      : Change directory               📂 ║")
    print(
        f"║ {Colors.GREEN}tree{Colors.CYAN}    : Show file system tree          🌳 ║")
    print(
        f"║ {Colors.GREEN}run{Colors.CYAN}     : Execute algorithm scripts      ⚙️ ║")
    print(
        f"║ {Colors.GREEN}status{Colors.CYAN}  : Show simulated system stats    📊 ║")
    print(
        f"║ {Colors.GREEN}history{Colors.CYAN} : Show command history           📜 ║")
    print(
        f"║ {Colors.GREEN}help{Colors.CYAN}    : Show this menu                 ❓ ║")
    print(
        f"║ {Colors.GREEN}exit{Colors.CYAN}    : Shut down system               🛑 ║")
    print(f"╚════════════════════════════════════════════╝{Colors.ENDC}\n")


def print_header(text):
    print(f"\n{Colors.BLUE}>> {Colors.BOLD}{text}{Colors.ENDC}")
