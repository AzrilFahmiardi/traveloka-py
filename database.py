import sqlite3
from rich.console import Console


console = Console()

def create_connection():
    try:
        # Connects to SQLite database file, creates it if doesn't exist
        connection = sqlite3.connect('project_alpro.db')
        
        # Create user table if it doesn't exist
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        connection.commit()
        return connection
    except sqlite3.Error as e:
        console.print(f"[red]Error saat koneksi ke SQLite: {e}")
        return None


class Database:
    @staticmethod
    def get_users():
        conn = create_connection()
        if conn is None:
            return []
            
        cursor = conn.cursor()
        query = "SELECT username, password, uang FROM user"
        try:
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except sqlite3.Error as e:
            console.print(f"[red]Error mengambil data user: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def register(username, password):
        conn = create_connection()
        if conn is None:
            return False
            
        cursor = conn.cursor()
        query = "INSERT INTO user (username, password) VALUES (?, ?)"
        try:
            cursor.execute(query, (username, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            console.print("[yellow]Username sudah digunakan")
            return False
        except sqlite3.Error as e:
            console.print(f"[red]Error saat registrasi: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def topup_db(uang,username):
        conn = create_connection()
        if conn is None:
            return False
            
        cursor = conn.cursor()
        query = "UPDATE user SET uang = uang + ? WHERE username = ?"
        try:
            cursor.execute(query, (uang, username))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # console.print("[yellow]Uang telah ditambahkan")
            return False
        except sqlite3.Error as e:
            console.print(f"[red]Error saat topup: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def bayar_uang(uang,username):
        conn = create_connection()
        if conn is None:
            return False
            
        cursor = conn.cursor()
        query = "UPDATE user SET uang = uang - ? WHERE username = ?"
        try:
            cursor.execute(query, (uang, username))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            # console.print("[yellow]Uang telah ditambahkan")
            return False
        except sqlite3.Error as e:
            console.print(f"[red]Error saat bayar: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def get_ticket(kota_asal, kota_tujuan, tanggal):
            conn = create_connection()
            if conn is None:
                return []
                
            cursor = conn.cursor()
            query = "SELECT maskapai, seat_slot, jam_keberangkatan, jam_tiba, kelas, kota_asal, kota_tujuan, harga_tiket, tanggal, id_tiket FROM ticket  WHERE kota_asal=? AND kota_tujuan=? AND tanggal=?"
            try:
                cursor.execute(query,(kota_asal, kota_tujuan,tanggal))
                users = cursor.fetchall()
                return users
            except sqlite3.Error as e:
                console.print(f"[red]Error mengambil data ticket: {e}")
                return []
            finally:
                cursor.close()
                conn.close()
        
    
    def get_all_ticket():
        conn = create_connection()
        if conn is None:
            return []
            
        cursor = conn.cursor()
        query = "SELECT maskapai, seat_slot, jam_keberangkatan, jam_tiba, kelas, kota_asal, kota_tujuan, harga_tiket, tanggal, id_tiket FROM ticket "
        try:
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except sqlite3.Error as e:
            console.print(f"[red]Error mengambil data ticket: {e}")
            return []
        finally:
            cursor.close()

    def get_ticket_byid(id):
            conn = create_connection()
            if conn is None:
                return []
                
            cursor = conn.cursor()
            query = "SELECT maskapai, seat_slot, jam_keberangkatan, jam_tiba, kelas, kota_asal, kota_tujuan, harga_tiket, tanggal, id_tiket FROM ticket  WHERE id_tiket=?"
            try:
                cursor.execute(query,(id,))
                users = cursor.fetchall()
                return users
            except sqlite3.Error as e:
                console.print(f"[red]Error mengambil data ticket: {e}")
                return []
            finally:
                cursor.close()
                conn.close()

    def pemesanan(a,b,c,d,e,f,g,h,i,j):
        conn = create_connection()
        if conn is None:
            return False
            
        cursor = conn.cursor()
        query = "INSERT INTO pemesanan (maskapai, nomor_penerbangan, nama_pemesan, perjalanan, jam_berangkat, jam_tiba, tgl_berangkat, total_pembayaran,jml_penumpang, status) VALUES (?, ?,?,?,?,?,?,?,?,?)"
        try:
            cursor.execute(query, (a,b,c,d,e,f,g,h,i,j))
            conn.commit()
            return True
        except sqlite3.Error as e:
            console.print(f"[red]Error saat insert pemesanan: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def get_all_pemesanan():
        conn = create_connection()
        if conn is None:
            return []
            
        cursor = conn.cursor()
        query = "SELECT maskapai, nomor_penerbangan, nama_pemesan, perjalanan, jam_berangkat, jam_tiba, tgl_berangkat, total_pembayaran,jml_penumpang, status FROM pemesanan "
        try:
            cursor.execute(query)
            pemesanan = cursor.fetchall()
            return pemesanan
        except sqlite3.Error as e:
            console.print(f"[red]Error mengambil data pemesanan: {e}")
            return []
        finally:
            cursor.close()


    def get_all_user():
        conn = create_connection()
        if conn is None:
            return []
            
        cursor = conn.cursor()
        query = "SELECT id, username, uang FROM user "
        try:
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except sqlite3.Error as e:
            console.print(f"[red]Error mengambil data users: {e}")
            return []
        finally:
            cursor.close()

    
            
