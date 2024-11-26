import os
import keyboard
import time
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from database import Database


console = Console()
terminal_width = os.get_terminal_size().columns
form_width = 40 
left_padding = (terminal_width - form_width) // 2
padding = " " * left_padding


def pause():
    print("\nTekan Enter untuk kembali ke menu utama...")
    while keyboard.is_pressed('enter'):
        pass
    while not keyboard.is_pressed('enter'):
        time.sleep(0.05)
    while keyboard.is_pressed('enter'):
        pass

def print_panel(
    content_items,
    panel_title=None,
    panel_width=100,
    content_width=96,
    panel_style="green",
    center_align=True
):
    console = Console()
    
    content = Text()
    
    for i, item in enumerate(content_items):
        if i > 0:
            content.append("\n")
        if isinstance(item, tuple):
            text, style = item
            if center_align:
                padding = (content_width - len(text)) // 2
                content.append(" " * padding)
            content.append(text, style=style)
        else:
            if center_align:
                padding = (content_width - len(item)) // 2
                content.append(" " * padding)
            content.append(item)
    
    panel = Panel(
        Align.center(content) if center_align else content,
        width=panel_width,
        title=panel_title,
        border_style=panel_style,
        padding=(1, 2)
    )
    
    console.print(Align.center(panel))

def print_menu(index):
    title = Text("Apakah anda sudah mempunyai akun?", style="bold green")
    title.align("center", width=96) 
    menu_items_top = ["History Pemesanan", "Daftar User"]
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
    loginRegisterPanel = Panel(
        Align.center(content),
        width=100,
        title="LOGIN OR REGISTER",
        border_style="green",
        padding=(1, 2)
    )
    console.print(Align.center(loginRegisterPanel))

def history_pemesanan():
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    console.print('[red]history pemesanan')
    pemesanan = Database.get_all_pemesanan()
    print(pemesanan)

    pause()
    
def daftar_user():
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    console.print('[red]dafta user')
    users = Database.get_all_user()
    print(users)

    pause()


def admin_menu(user_session):
    index_menu = 0
    last_key = None
    
    while True:
        os.system("cls")
        print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
        print_menu(index_menu)

        if keyboard.is_pressed("right") and last_key != "right":
            index_menu = 1
            last_key = "right"
        elif keyboard.is_pressed("left") and last_key != "left":
            index_menu = 0
            last_key = "left"
        elif keyboard.is_pressed("q") and last_key != "a":
            return
        elif keyboard.is_pressed("enter") and last_key != "enter":
            if index_menu == 0:
                history_pemesanan()
            elif index_menu == 1:
                daftar_user()
            last_key = "enter"

        if not (keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter") or keyboard.is_pressed("r") or keyboard.is_pressed("left") or keyboard.is_pressed("right")):
            last_key = None

        time.sleep(0.05) 


    pause()