import os
import keyboard
import time
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.progress import Progress



from database import Database
import pesanDanBayar as pb

console = Console()



terminal_width = os.get_terminal_size().columns
form_width = 55 
left_padding = (terminal_width - form_width) // 2
padding = " " * left_padding

class Ticketing:
    def __init__(self, kota_asal, kota_tujuan, tanggal ) :
        data = Database.get_ticket(kota_asal, kota_tujuan, tanggal)
        self.template_end_start = '='*50
        self.data_tiket = data
        self.data_fitur = ['Ubah Tanggal: ', 'Ubah Keberangkatan: ', 'Ubah Tujuan: ','Filter: ', 'Berdasarkan Harga: ', 'Berdasarkan Jam Keberangkatan: ', 'Berdasarkan Maskapai: ', 'Berdasarkan Kelas: ', '(Q Untuk Kembali)'] 
        self.data_temp_filter = []
        
        
    def format(self):
        for indeks in range (11) :
            if indeks == 0 or indeks == 10: 
                print(self.template_end_start)
            else:
                for i in range(len(self.template_end_start)):
                    if i == 0 :
                        print('|', end='')
                    elif i == len(self.template_end_start)-1:
                        print('|')
                    elif i == 1 or i == len(self.template_end_start)-2:
                        print(end=' ')
                    else :
                        if i-2 < len(self.data_fitur[indeks-1]):
                            print(self.data_fitur[indeks-1][i-2], end='')
                        else: 
                            print(end=' ')
                            
    def format_header(self):
        for i in range(4):
            if i == 0 or i == 2 :
                print(self.template_end_start)
            elif i == 1 :
                print('|' + format('LIST TIKET PESAWAT', ' ^48')+ '|')                          
            else:
                print('Pilih Nomer Tiket Untuk Memesan Tiket')
    
    def format_tiket(self):
        for p in range(len(self.data_tiket)):
            for baris in range (5) :
                if baris == 0 or baris == 4  :
                    print(self.template_end_start)
                else:
                    kolom = 0
                    for i in range(3) :
                        if i == 0 :    
                            print('|', end=' ')
                            kolom += 2
                        elif i == 2 :
                            print('|') 
                        else :
                            if baris == 1:
                                console.print(f'[cyan]{p+1}.', end=' ')
                                kolom += len(str(p+1)) + 2
                                panjang1 = len(self.data_tiket[p][0])
                                panjang2 = len(str(self.data_tiket[p][1])) + 9
                                tambahan = 48 - kolom - panjang2 - panjang1
                                console.print('[cyan]'+self.data_tiket[p][0] + '(' + str(self.data_tiket[p][9]) + ')'+ '[white]'+ ' '*(tambahan-5 )+ str(self.data_tiket[p][1]) + ' Tersedia', end=' ')
                            elif baris == 2 :
                                panjang1 = 14
                                panjang2 = len(self.data_tiket[p][4])
                                panjang3 = 11

                                tambahan = 48 - kolom - panjang1 - panjang2 - panjang3
                                print(f'{self.data_tiket[p][2]} -- {self.data_tiket[p][3]}' +    f' {self.data_tiket[p][8]}'   +  ' '*tambahan + self.data_tiket[p][4], end=' ')
                            else :
                                panjang1 = len(self.data_tiket[p][5]) + len(self.data_tiket[p][6]) + 4
                                panjang2 = len(str(self.data_tiket[p][7])) + 2 
                                tambahan = 48 - kolom - panjang1 - panjang2
                                print(f'{self.data_tiket[p][5]} -- {self.data_tiket[p][6]}' + ' '*tambahan + f'Rp{self.data_tiket[p][7]}', end=' ' )

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

def list_tiket(kota_asal, kota_tujuan, tanggal):
    a= Ticketing(kota_asal, kota_tujuan, tanggal)
    # b = a.format()
    d= a.format_header()
    c= a.format_tiket()


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

def loading_bar():
    with Progress() as progress:
        task = progress.add_task(padding + "[cyan]Loading...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.03)
    # Prompt.ask("Press Enter to continue...")  # Menunggu enter untuk lanjut

def cari_tiket():
    clear_input_buffer()
    print(padding + "----------------------------------------------------")
    print(padding + "|               🔎 CARI TIKET PERJALANAN           |")
    print(padding + "----------------------------------------------------")
    kota_asal = input(padding + "🏙️ Kota Asal          : ")
    kota_tujuan = input(padding + "🏙️ Kota Tujuan        : ")
    tanggal = input(padding + "📅 Tanggal Keberangkatan (dd-mm-yyyy) : ")
    
    # print("\n" + padding + "----------------------------------------------------")
    # print(padding + "|               🎫 PILIH KELAS PERJALANAN          |")
    # print(padding + "----------------------------------------------------")
    # print(padding + "   [1] Ekonomi")
    # print(padding + "   [2] Bisnis")
    # print(padding + "   [3] Eksekutif")
    
    # while True:
    #     try:
    #         pilihan_kelas = int(input("\n" + padding +  "> Pilih kelas dengan mengetik nomor: "))
    #         if pilihan_kelas not in [1, 2, 3]:
    #             raise ValueError(padding + "Nomor yang dimasukkan harus 1, 2, atau 3.")
    #         break
    #     except ValueError as e:
    #         print(padding + f"Input tidak valid: {e}")
    
    # kelas = {1: "Ekonomi", 2: "Bisnis", 3: "Eksekutif"}[pilihan_kelas]
    
    print("\n" +  padding +  "----------------------------------------------------")
    console.print(padding + "[green][ Cari Tiket ]                              [red][ Batal ]")
    print(padding + "----------------------------------------------------")
    
    while True:
        konfirmasi = input("\n" + padding + "> Ketik 'Cari' untuk melanjutkan atau 'Batal' untuk membatalkan\n " + padding + ": ").strip().lower()
        if konfirmasi == "cari":
            print("\n" +  padding +  "Pencarian tiket sedang diproses...")
            loading_bar()
            return {'asal':kota_asal, 'tujuan':kota_tujuan, 'tanggal': tanggal}
        elif konfirmasi == "batal":
            print("\n" +  padding +  "Pencarian tiket dibatalkan.")
            break
        else:
            print(padding + "Input tidak valid. Harap ketik 'Cari' atau 'Batal'.")

def pesawat(index, user_session):
    filter = None

    while True:
        os.system("cls")
    
        if filter == None:
            if user_session:
                print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")
        print()
    
        if filter is None:
            # Memanggil pencarian tiket jika filter belum diatur
            filter = cari_tiket()
            if not filter:  # Jika pengguna membatalkan pencarian
                break
        else:
            os.system('cls')
            print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")
            asal = filter['asal']
            tujuan = filter['tujuan']
            tanggal = filter['tanggal']
            list_tiket(asal,tujuan,tanggal)
            

            id_tiket = console.input("[green]Masukkan id tiket: ")
            print('id tiket yg dipilih : ', id_tiket)
            # detail_tiket(id_tiket, user_session)
            updated_session = pb.menu(id_tiket, user_session)



            pause()
            return updated_session