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
    
    # Add bottom menu items (centered)
    menu_text.append("\n\n")
    for item in menu_items_bottom:
        bottom_text = f"  {item}"
        padding = (max_width - len(bottom_text)) // 2
        menu_text.append(" " * padding + bottom_text)
    
    # Navigation text - perbaikan centering
    nav_text = "← → : Navigate Menu | Enter : Select | r : Login/Registrate"
    padding = (max_width - len(nav_text)) // 2
    navigation = Text("\n\n" + " " * padding + nav_text)
    
    # Combine all content
    content = Text.assemble(
        title, "\n\n",
        menu_text, "\n",
        navigation
    )
    
    # Create and display panel with center aligned content
    welcome_panel = Panel(
        Align.center(content),
        width=100,
        title="Main Menu",
        border_style="green",
        padding=(1, 2)
    )
    
    # Print the panel
    console.print(Align.center(welcome_panel))
    

def main():
    index_menu = 0
    last_key = None
    while True:
        os.system("cls")
        # print_header()
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
            loginOrRegister(index_menu)
            last_key = "r"

        if not (keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter") or keyboard.is_pressed("r") or keyboard.is_pressed("left") or keyboard.is_pressed("right")):
            last_key = None

        time.sleep(0.05) 
    

if __name__ == "__main__":
    main()

