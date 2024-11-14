import mysql.connector
from rich.console import Console

console = Console()


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="12345678",   
            database="project_alpro" 
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error saat koneksi ke MySQL: {e}")
        return None


class Database:
    def get_users():
        conn = create_connection()
        cursor = conn.cursor()
        query = "SELECT username, password FROM user"
        try:
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except Exception as e:
            console.print(f"[red]Error mengambil data user: {e}")
            return []
        finally:
            cursor.close()
            conn.close() 

    def register(username, password):
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO user (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(query, (username, password))
            conn.commit()
            console.print(f"\n[green]User {username} berhasil terdaftar!")
        except Exception as e:
            console.print(f"[red]Error mendaftar user: {e}")
        finally:
            cursor.close()
            conn.close() 