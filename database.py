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