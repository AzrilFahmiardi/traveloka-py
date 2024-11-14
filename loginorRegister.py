from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
import time
import keyboard
import os

from database import Database

console = Console()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        users = Database.get_users()
        for user in users:
            if user[0] == self.username and user[1] == self.password:
                return True
        return False
    
    def register(self):
        Database.register(self.username,self.password)
    

def pause():
    print("\nTekan Enter untuk kembali ke menu utama...")
    while keyboard.is_pressed('enter'):
        pass
    while not keyboard.is_pressed('enter'):
        time.sleep(0.05)
    while keyboard.is_pressed('enter'):
        pass

def clear_input_buffer():
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            _ = msvcrt.getch()
    
def print_menu(index):
    title = Text("Apakah anda sudah mempunyai akun?", style="bold green")
    title.align("center", width=96) 
    
    menu_items_top = [
        "Login", 
        "Register"
    ]
    
    
    menu_text = Text()
    
    max_width = 96
    
    top_menu_items = []
    for i, item in enumerate(menu_items_top):
        if i == index:
            top_menu_items.append(f"> {item}")
        else:
            top_menu_items.append(f"  {item}")
    
    top_menu_str = "    ".join(top_menu_items)
    padding = (max_width - len(top_menu_str)) // 2
    menu_text.append(" " * padding)
    
    for i, item in enumerate(menu_items_top):
        if i == index:
            menu_text.append(f"> {item}", style="cyan")
        else:
            menu_text.append(f"  {item}")
            
        if i < len(menu_items_top) - 1:
            menu_text.append("    ")
    
    menu_text.append("\n\n")

    
    nav_text = "← → : Navigate Menu | Enter : Select | q : Main Menu"
    padding = (max_width - len(nav_text)) // 2
    navigation = Text("\n\n" + " " * padding + nav_text)
    
    content = Text.assemble(
        title, "\n\n",
        menu_text, "\n",
        navigation
    )
    
    welcome_panel = Panel(
        Align.center(content),
        width=100,
        title="LOGIN OR REGISTER",
        border_style="green",
        padding=(1, 2)
    )
    
    console.print(Align.center(welcome_panel))

def login():
    os.system("cls")
    console.print('Login\n')

    clear_input_buffer()

    username = console.input("[cyan]Username: ")
    password = console.input("[cyan]Password: ")

    user = User(username, password)
    if user.login(): 
        console.print("\n[green]Login successful!")
    else:
        console.print("\n[red]Username or password is incorrect.")

    pause()


def register():
    os.system("cls")
    print('register\n')

    clear_input_buffer()

    username = console.input("[cyan]Username: ")
    password = console.input("[cyan]Password: ")

    user = User(username,password)
    user.register()

    pause()


def loginOrRegister(index):
    index_menu = 0
    last_key = None
    while True:
        os.system("cls")
        print_menu(index_menu)


        if keyboard.is_pressed("right") and last_key != "right":
            index_menu = 1
            last_key = "right"
        elif keyboard.is_pressed("left") and last_key != "left":
            index_menu = 0
            last_key = "left"
        elif keyboard.is_pressed("q") and last_key != "left":
            return
        elif keyboard.is_pressed("enter") and last_key != "enter":
            if index_menu == 0:
               login()
            elif index_menu == 1:
                register()
            last_key = "enter"

        if not (keyboard.is_pressed("enter") or  keyboard.is_pressed("left") or keyboard.is_pressed("right")):
            last_key = None

        time.sleep(0.05)

if __name__ == "__main__":
    loginOrRegister()
    

