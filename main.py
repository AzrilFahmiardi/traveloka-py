import os
import time
import keyboard
from colorama import Fore, Style, init
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich import align
from rich.align import Align
from rich.layout import Layout
from rich.columns import Columns
from termcolor import colored

from pesawat import *
from kereta import *
from loginorRegister import *

import getpass

init()
console = Console()

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
    title = Text("WELCOME TO RPLTICKET", style="bold green")
    title.align("center", width=96) 
    
    menu_items_top = [
        "Pesawat", 
        "Kereta"
    ]
    
    menu_items_bottom = [
        "Login/Registrasi (r)"
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
    for item in menu_items_bottom:
        bottom_text = f"  {item}"
        padding = (max_width - len(bottom_text)) // 2
        menu_text.append(" " * padding + bottom_text)
    
    nav_text = "← → : Navigate Menu | Enter : Select | r : Login/Registrate"
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
        title="Main Menu",
        border_style="green",
        padding=(1, 2)
    )
    
    console.print(Align.center(welcome_panel))

def main():
    index_menu = 0
    last_key = None
    user_session = None

    while True:
        os.system("cls")
        if user_session:
            print_panel([f"logged in as :  {user_session['username']}"], center_align=False, panel_style="cyan")
        print_menu(index_menu)

        if keyboard.is_pressed("right") and last_key != "right":
            index_menu = 1
            last_key = "right"
        elif keyboard.is_pressed("left") and last_key != "left":
            index_menu = 0
            last_key = "left"
        elif keyboard.is_pressed("up") and last_key != "up":
            index_menu = 0  
            last_key = "up"
        elif keyboard.is_pressed("enter") and last_key != "enter":
            if index_menu == 0:
               pesawat(index_menu)
            elif index_menu == 1:
                kereta(index_menu)
            last_key = "enter"
        elif keyboard.is_pressed("r") and last_key != "r":
            user_session = loginOrRegister(index_menu)
            last_key = "r"

        if not (keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter") or keyboard.is_pressed("r") or keyboard.is_pressed("left") or keyboard.is_pressed("right")):
            last_key = None

        time.sleep(0.05) 

if __name__ == "__main__":
    main()
