import os
import keyboard
import time
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
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

def clear_input_buffer():
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            _ = msvcrt.getch()

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

def merge_sort(arr,menu, order):
    if len(arr) <= 1:
        return arr
    
    divide = len(arr)//2
    right = arr[divide:]
    left = arr[:divide]

    right_sorted = merge_sort(right, menu, order)
    left_sorted = merge_sort(left, menu, order)

    return merge(right_sorted, left_sorted,menu, order)

def merge(right, left, menu, order):
    merged = []
    i = j = 0

    if order == 1:
        while i < len(left) and j < len(right):
            if left[i][menu] < right[j][menu]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
    elif order == 2:
        while i < len(left) and j < len(right):
            if left[i][menu] > right[j][menu]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def menu_search() :
    clear_input_buffer()
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    console.print(padding + '[green]Silahkan Pilih History Yang Ingin Ditampilkan: \n')
    print(padding + '1. Tampilkan Semua')
    print(padding + '2. Berdasarkan Maskapai')
    print(padding + '3. Berdasarkan Kota Tujuan')
    try:     
        interaction = int(console.input('\n' + padding + 'Pilih Menu ([red]4 Untuk Kembali[white]): '))
        if interaction == 1 :
            history_pemesanan()
        elif interaction == 2 :
            history_maskapai()
        elif interaction == 3:
            history_kota_tujuan()
        elif interaction == 4 :
            return
        else:
            raise ValueError
    except ValueError or TypeError :
            print('Harap Pilih Dengan Benar')
            menu_search()

def history_maskapai():
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    pemesanan = Database.get_all_pemesanan()
    data_filter = []
    maskapai = console.input(padding + '[red]Masukkan Maskapai: ')
    
    for data in pemesanan: 
        if maskapai in data[0] :
            data_filter.append(data)
            
    padding_10 = " " * 10 
    naziri=[(format("Maskapai","<19")),(format("Nomor Penerbangan","<19")),(format("Nama Pemesan","<19")),(format("Perjalanan","<19")),(format("Jam Keberangkatan","<19")),(format("Jam tiba","<19")),(format("Tgl. Keberangkatan","<19")),(format("Total Pembayaran","<19")),(format("Jumlah Penumpang","<19")),(format("Status","<19"))]
    for i in data_filter:
        for j in range(10):
            if j==0:
                console.print(padding_10 + "[green]" + "="*50, justify="center")
                console.print(padding_10 + f"[bold yellow]KARTU PENDAFTARAN ({i[2]})\n", justify="center")
            console.print(f"{padding}[cyan]{naziri[j]}:[/cyan] [white]{i[j]}[/white]")
        console.print(padding_10 + "[green]" + "="*50, justify="center")
    pause()

def history_kota_tujuan():
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    
    pemesanan = Database.get_all_pemesanan()
    data_filter = []
    tujuan = console.input(padding + '[red]Masukkan tujuan: ')
    for data in pemesanan: 
        temp = str(data[3]).split(' - ')
        destinasi = temp[1]
        if tujuan in destinasi :
            data_filter.append(data)
    
    padding_10 = " " * 10 
            
    naziri=[(format("Maskapai","<19")),(format("Nomor Penerbangan","<19")),(format("Nama Pemesan","<19")),(format("Perjalanan","<19")),(format("Jam Keberangkatan","<19")),(format("Jam tiba","<19")),(format("Tgl. Keberangkatan","<19")),(format("Total Pembayaran","<19")),(format("Jumlah Penumpang","<19")),(format("Status","<19"))]
    for i in data_filter:
        for j in range(10):
            if j==0:
                console.print(padding_10 + "[green]" + "="*50, justify="center")
                console.print(padding_10 + f"[bold yellow]KARTU PENDAFTARAN ({i[2]})\n", justify="center")
        for j in range(10):
            console.print(f"{padding}[cyan]{naziri[j]}:[/cyan] [white]{i[j]}[/white]")
        console.print(padding_10 + "[green]" + "="*50, justify="center")
    pause()

def history_pemesanan():
    os.system("cls")
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    
    pemesanan = Database.get_all_pemesanan()
    naziri = [
        (format("Maskapai", "<19")),
        (format("Nomor Penerbangan", "<19")),
        (format("Nama Pemesan", "<19")),
        (format("Perjalanan", "<19")),
        (format("Jam Keberangkatan", "<19")),
        (format("Jam tiba", "<19")),
        (format("Tgl. Keberangkatan", "<19")),
        (format("Total Pembayaran", "<19")),
        (format("Jumlah Penumpang", "<19")),
        (format("Status", "<19"))
    ]
    
    padding_10 = " " * 10 

    for i in pemesanan:
        console.print(padding_10 + "[green]" + "="*50, justify="center")
        console.print(padding_10 + f"[bold yellow]KARTU PENDAFTARAN ({i[2]})\n", justify="center")
        for j in range(10):
            console.print(f"{padding}[cyan]{naziri[j]}:[/cyan] [white]{i[j]}[/white]")
        console.print(padding_10 + "[green]" + "="*50, justify="center")
        print()
    pause()
    
def daftar_user():
    os.system("cls")
    clear_input_buffer()
    print_panel([f"logged in as :  admin\t\t\t\t\t\t\t    "], center_align=False, panel_style="cyan")
    users = Database.get_all_user()
    # print(users)
    console.print("=" * 60, style="bold magenta", justify="center")
    console.print("[bold white]Pilih kriteria pengurutan:[/bold white]", justify="center")
    console.print("[bold magenta]1. Berdasarkan Nama (Abjad)[/bold magenta]", justify="center")
    console.print("[bold magenta]2. Berdasarkan Saldo[/bold magenta]", justify="center")
    console.print("=" * 60, style="bold magenta", justify="center")
    while True:
        try:
            sort_menu = int(input('Piilh berdasarkan angka: '))
            if sort_menu not in [1, 2]:
                console.print("[bold red]Pilih angka 1 atau 2![/bold red]")
            else:
                break
        except ValueError:
            console.print("[bold red]Input harus berupa angka![/bold red]")
            input('enter')
    console.print("=" * 60, style="bold magenta", justify="center")
    console.print("[bold white]Pilih urutan:[/bold white]", justify="center")
    console.print("[bold magenta]1. Ascending[/bold magenta]", justify="center")
    console.print("[bold magenta]2. Descending[/bold magenta]", justify="center")
    console.print("=" * 60, justify="center")
    while True:
        try:
            sort_order = int(input("Pilih urutan (1 atau 2): "))
            if sort_order not in [1, 2]:
                console.print("[bold red]Pilih angka 1 atau 2![/bold red]")
            else:
                break
        except ValueError:
            console.print("[bold red]Input harus berupa angka![/bold red]")
    
    console.clear()
        
    sorted_data = merge_sort(users, sort_menu, sort_order)

        
    # Tampilkan judul tabel
    console.print("=" * 60, style="bold magenta", justify="center")
    console.print("[bold white]Daftar Pengguna[/bold white]", justify="center")
    console.print("=" * 60, style="bold magenta", justify="center")
    
    # Membuat tabel
    table = Table(style="bold magenta")
    table.add_column("No", justify="center", style="bold cyan")
    table.add_column("Nama", justify="left", style="bold magenta")
    table.add_column("Saldo", justify="right", style="bold green")


    # Menambahkan baris ke tabel
    for item in sorted_data:
        table.add_row(str(item[0]), item[1], f"Rp {item[2]:,}")

    # Print table with center alignment
    console.print(table, justify="center")

    # Pilihan untuk kembali ke menu utama atau keluar
    console.print("=" * 60, style="bold magenta", justify="center")
    console.print("[bold white]1. Kembali ke Menu Utama[/bold white]", justify="center")
    console.print("[bold red]2. Keluar[/bold red]", justify="center")
    console.print("=" * 60, style="bold magenta", justify="center")

    while True:
        try:
            option = int(input("Pilih opsi (1 atau 2): "))
            if option == 1:
                console.clear()
                break
            elif option == 2:
                console.print("[bold green]Terima kasih! Program selesai.[/bold green]")
                return
            else:
                console.print("[bold red]Pilih angka 1 atau 2![/bold red]")
        except ValueError:
            console.print("[bold red]Input harus berupa angka![/bold red]")

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
                menu_search()
            elif index_menu == 1:
                daftar_user()
            last_key = "enter"

        if not (keyboard.is_pressed("down") or keyboard.is_pressed("up") or keyboard.is_pressed("enter") or keyboard.is_pressed("r") or keyboard.is_pressed("left") or keyboard.is_pressed("right")):
            last_key = None

        time.sleep(0.05) 


    pause()