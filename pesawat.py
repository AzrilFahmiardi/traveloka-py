import os
import keyboard
import time
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.text import Text

terminal_width = os.get_terminal_size().columns
form_width = 55 
left_padding = (terminal_width - form_width) // 2
padding = " " * left_padding

def clear_input_buffer():
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            _ = msvcrt.getch()

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

def cari_tiket():
    clear_input_buffer()
    print(padding + "----------------------------------------------------")
    print(padding + "|               🔎 CARI TIKET PERJALANAN           |")
    print(padding + "----------------------------------------------------")
    kota_asal = input(padding + "🏙️ Kota Asal          : ")
    kota_tujuan = input(padding + "🏙️ Kota Tujuan        : ")
    tanggal = input(padding + "📅 Tanggal Keberangkatan (dd-mm-yyyy) : ")
    
    print("\n" + padding + "----------------------------------------------------")
    print(padding + "|               🎫 PILIH KELAS PERJALANAN          |")
    print(padding + "----------------------------------------------------")
    print(padding + "   [1] Ekonomi")
    print(padding + "   [2] Bisnis")
    print(padding + "   [3] Eksekutif")
    
    while True:
        try:
            pilihan_kelas = int(input("\n" + padding +  "> Pilih kelas dengan mengetik nomor: "))
            if pilihan_kelas not in [1, 2, 3]:
                raise ValueError(padding + "Nomor yang dimasukkan harus 1, 2, atau 3.")
            break
        except ValueError as e:
            print(padding + f"Input tidak valid: {e}")
    
    kelas = {1: "Ekonomi", 2: "Bisnis", 3: "Eksekutif"}[pilihan_kelas]
    
    print("\n" +  padding +  "----------------------------------------------------")
    print(padding + "[ Cari Tiket ]                              [ Batal ]")
    print(padding + "----------------------------------------------------")
    
    while True:
        konfirmasi = input("\n> Ketik 'Cari' untuk melanjutkan atau 'Batal' untuk membatalkan: ").strip().lower()
        if konfirmasi == "cari":
            print("\n" +  padding +  "Pencarian tiket sedang diproses...")
            print(padding + f"Kota Asal         : {kota_asal}")
            print(padding + f"Kota Tujuan       : {kota_tujuan}")
            print(padding + f"Tanggal Keberangkatan : {tanggal}")
            print(padding + f"Kelas Perjalanan  : {kelas}")
            break
        elif konfirmasi == "batal":
            print("\n" +  padding +  "Pencarian tiket dibatalkan.")
            break
        else:
            print(padding + "Input tidak valid. Harap ketik 'Cari' atau 'Batal'.")

def pesawat(index, user_session):
    os.system("cls")
    if user_session:
        print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")
    print()
    cari_tiket()
    
    pause()