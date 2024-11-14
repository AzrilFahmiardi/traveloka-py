from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
import time
import keyboard
import os

console = Console()

def print_frame(menu_items_top=None, menu_items_bottom=None, nav_text=None, width=96):
    # Initialize menu text
    menu_text = Text()

    # Process top menu items (optional)
    if menu_items_top is not None:
        top_menu_items = []
        for i, item in enumerate(menu_items_top):
            top_menu_items.append(f"> {item}" if i == 0 else f"  {item}")

        top_menu_str = "    ".join(top_menu_items)
        padding = (width - len(top_menu_str)) // 2
        menu_text.append(" " * padding)
        
        for i, item in enumerate(menu_items_top):
            menu_text.append(f"> {item}" if i == 0 else f"  {item}", style="cyan" if i == 0 else "")
            if i < len(menu_items_top) - 1:
                menu_text.append("    ")

    # Add bottom menu items (optional)
    if menu_items_bottom is not None:
        menu_text.append("\n\n")  # Add space between top and bottom menu
        for item in menu_items_bottom:
            bottom_text = f"  {item}"
            padding = (width - len(bottom_text)) // 2
            menu_text.append(" " * padding + bottom_text)

    # Navigation text (optional)
    if nav_text is not None:
        padding = (width - len(nav_text)) // 2
        navigation = Text("\n\n" + " " * padding + nav_text)
        menu_text.append(navigation)

    # Combine all content
    content = Text.assemble(menu_text)

    # Create and display the panel with centered content
    welcome_panel = Panel(
        Align.center(content),
        width=width + 4,  # Slightly wider for the border
        title="Register or Login",
        border_style="green",
        padding=(1, 2)
    )

    # Print the panel
    console.print(Align.center(welcome_panel))

def pause():
    print("\nTekan Enter untuk kembali ke menu utama...")
    while keyboard.is_pressed('enter'):
        pass
    while not keyboard.is_pressed('enter'):
        time.sleep(0.05)
    while keyboard.is_pressed('enter'):
        pass

def menu():
    menu_items_top = [
        "Login", 
        "Register"
    ]
    menu_items_bottom = [
        "Press 'r' to return to main menu"
    ]
    nav_text = "← → : Navigate Menu | Enter : Select | r : Login/Registrate"
    print_frame(menu_items_top, menu_items_bottom, nav_text)

def loginOrRegister(index):
    os.system("cls")
    print_frame(menu_items_top=["Login", "Register"])
    pause()

# Call the menu function to test
menu()
