import time
import random
from database import Database
import os
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import keyboard
from rich.progress import Progress


terminal_width = os.get_terminal_size().columns
form_width = 40 
left_padding = (terminal_width - form_width) // 2
padding = " " * left_padding

console = Console()


class Pemesan:
    data = Database.get_all_ticket()
    db = []
    namaPemesan = None

    def __init__(self,nama,email, id_tiket):
        self.__nama = nama
        self.__email = email
        self.__noReg = id_tiket
        self.__dbpenumpang = []
        Pemesan.db.append(self)

    @property
    def gender(self):
        return self.__gender
    @property
    def nama(self):
        return self.__nama
    @property
    def noHP(self):
        return self.__noHP
    @property
    def email(self):
        return self.__email
    @property
    def dbpenumpang(self):
        return self.__dbpenumpang
    @property
    def noReg(self):
        return self.__noReg
    
    # Method db.txt
    def inputDatabase(self):
        teks = ''
        for penumpang in self.dbpenumpang:
            teks += penumpang.nama + ", "
        Database.order(self.nama, teks, self.noReg)
        

class Penumpang(Pemesan):

    def __init__(self, gender, nama):
        self.__gender = gender
        self.__nama = nama
        if Pemesan.namaPemesan:
            Pemesan.namaPemesan.dbpenumpang.append(self)
    
    @property
    def gender(self):
        return self.__gender
    @property
    def nama(self):
        return self.__nama

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

def pause():
    print(f"\n{padding}Tekan Enter untuk kembali ke menu utama...")
    while keyboard.is_pressed('enter'):
        pass
    while not keyboard.is_pressed('enter'):
        time.sleep(0.05)
    while keyboard.is_pressed('enter'):
        pass

def loading_bar():
    with Progress() as progress:
        task = progress.add_task(padding + "[cyan]Loading...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.02)

def idPemesan(id, user):
    print(padding + f'Nama Pemesan\t\t: {user['username']}')
    print(padding + f'ID Tiket\t\t: {id}')
    namaPemesan  = user['username']
    id_tiket = id
    
    

    emailPemesan = input(padding + "Alamat email \t: ")

    # Pemesan.namaPemesan = Pemesan(genderPemesan, namaPemesan, HPPemesan, emailPemesan)
    Pemesan.namaPemesan = Pemesan(namaPemesan, emailPemesan, id_tiket)


def idPenumpang():
    global total_harga
    try:
        jmlPenumpang = int(input(padding + 'Jumlah penumpang: '))
    except ValueError:
        print(padding + 'MASUKKAN ANGKA!!!!')
        jmlPenumpang = int(input(padding + "="*50+'\n' + padding + 'Jumlah penumpang \t: '))
    total_harga = jmlPenumpang * Penumpang.data[0][7]

    console.print('\n' + padding + "[green]IDENTITAS PENUMPANG")
    for penumpang in range(jmlPenumpang):
        namaPenumpang = input(padding + f"Nama Penumpang ke-{penumpang+1}\t: ")
        new_penumpang = Penumpang("Pria", namaPenumpang)

def konfirmasiTiket(id):
    data = Database.get_ticket_byid(id)
    print(padding + f"""
{padding}DETAIL PEMESANAN 
{padding}Maskapai \t\t: {data[0][0]}
{padding}Perjalanan\t\t: {data[0][5]} - {data[0][6]}
{padding}Jam keberangkatan\t: {data[0][2]}
{padding}Jam tiba\t\t: {data[0][3]}
{padding}Tgl. keberangkatan\t: {data[0][8]}
{padding}Total Pembayaran \t: {data[0][7]*len(Pemesan.namaPemesan.dbpenumpang)}
{padding}Penumpang \t\t: {len(Pemesan.namaPemesan.dbpenumpang)}
""")
    # print(data)
    console.input(padding +  '[green]Enter untuk lanjut ke pembayaran')

def pembayaran(user,id):
    data = Database.get_ticket_byid(id)
    metodePembayaran = int(input(f"""{padding}Pilih metode pembayaran:
{padding}# 1. rekening
{padding}# 2. Tunai
{padding}# Pilih angka \t: """))
    if metodePembayaran == 1:
        console.print(f'\n{padding}Jumlah saldo\t: [cyan]{user['uang']}')
        uang = int(user['uang'])
        harga = total_harga
        if uang < harga:
            print(f'{padding}Uang anda tidak cukup, silakan topup terlebih dahulu\n{padding}harga tiket : {harga}')
            return
        
        
        temp = console.input(f'{padding}Harga tiket\t: [green]{harga}\n{padding}[white]Proses pembayaran ? (y/n) : ')
        if temp == "y":
            print(padding + "Pembayaran sedang diproses...")
            loading_bar()
            console.print(f'\n{padding}Proses berhasil, saldo anda sekarang tersisa : [cyan]Rp.{uang - harga} \n')
            
            console.input(padding +  '[green]Enter untuk mencetak kartu pendaftaran')

            Database.bayar_uang(harga, user['username'])
            session = {'username': user['username'], 'uang': uang-harga, 'logged_in': True}
        else:
            pause()
            return
        
        
        os.system("cls")
        print()
        print()
        print()

        console.print(padding + "="*50+f"""\n{padding}[cyan]KARTU PENDAFTARAN[white]
{padding}Maskapai \t\t: {data[0][0]}
{padding}Nomor penerbangan \t: {Pemesan.namaPemesan.noReg}
{padding}Nama pemesan \t: {Pemesan.namaPemesan.nama}
{padding}Perjalanan\t\t: {data[0][5]} - {data[0][6]}
{padding}Jam keberangkatan\t: {data[0][2]}
{padding}Jam tiba\t\t: {data[0][3]}
{padding}Tgl. keberangkatan\t: {data[0][8]}
{padding}Total Pembayaran \t: {data[0][7]*len(Pemesan.namaPemesan.dbpenumpang)}
{padding}Jumlah Penumpang\t: {len(Pemesan.namaPemesan.dbpenumpang)}
{padding}Status: Lunas""")
        Database.pemesanan(data[0][0],Pemesan.namaPemesan.noReg,Pemesan.namaPemesan.nama, f'{data[0][5]} - {data[0][6]}', data[0][2], data[0][3], data[0][8],data[0][7]*len(Pemesan.namaPemesan.dbpenumpang), len(Pemesan.namaPemesan.dbpenumpang), "Lunas"   )
        return session

    elif metodePembayaran == 2:
        os.system("cls")
        print()
        print()
        print()

        console.print(padding + "="*50+f"""\n{padding}[cyan]KARTU PENDAFTARAN[white]
{padding}Maskapai \t\t: {data[0][0]}
{padding}Nomor penerbangan \t: {Pemesan.namaPemesan.noReg}
{padding}Nama pemesan \t: {Pemesan.namaPemesan.nama}
{padding}Perjalanan\t\t: {data[0][5]} - {data[0][6]}
{padding}Jam keberangkatan\t: {data[0][2]}
{padding}Jam tiba\t\t: {data[0][3]}
{padding}Tgl. keberangkatan\t: {data[0][8]}
{padding}Total Pembayaran \t: {data[0][7]*len(Pemesan.namaPemesan.dbpenumpang)}
{padding}Jumlah Penumpang\t: {len(Pemesan.namaPemesan.dbpenumpang)}
{padding}Status\t\t: Belum Lunas""")
        Database.pemesanan(data[0][0],Pemesan.namaPemesan.noReg,Pemesan.namaPemesan.nama, f'{data[0][5]} - {data[0][6]}', data[0][2], data[0][3], data[0][8],data[0][7]*len(Pemesan.namaPemesan.dbpenumpang), len(Pemesan.namaPemesan.dbpenumpang), "Belum Lunas"   )

        
        

def menu(id, user):
    os.system("cls")
    user_session = user
    if user_session:
        print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")
    
    
    print(padding + '='*50)
    idPemesan(id,user)
    print(padding + '='*50+'\n')
    print(padding + '='*50)
    idPenumpang()
    print(padding + '='*50+'\n')
    os.system("cls")
    print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")

    print(padding + '='*50)
    konfirmasiTiket(id)
    print(padding + '='*50)
    print('\n'+ padding + '='*50)
    os.system("cls")
    print_panel([f"logged in as :  {user_session['username']}\t\t\t\t\t\t\t    Uang : Rp {user_session['uang']}"], center_align=False, panel_style="cyan")
    session = pembayaran(user, id)
    print(padding + '='*50)
    # Pemesan.namaPemesan.inputDatabase()
    return session

# print(Pemesan.db[0].nama ,Pemesan.db[0].dbpenumpang[0].nama, pendaftaran)