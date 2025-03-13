import sqlite3
from encryption import encrypt_password, decrypt_password
connectString = "passwords.db"

def initialize_db():
    
    con = sqlite3.connect(connectString)
    cursor=con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()

def add_site(site,username,password): #kayıt ekler
    con=sqlite3.connect(connectString)
    cursor=con.cursor()
    cursor.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)", (site, username, password))
    con.commit()
    con.close()
    print(f"✅ {site} için şifre başarıyla kaydedildi.")

def get_all_password():
    con = sqlite3.connect(connectString)
    cursor = con.cursor()
    
    # Tüm kayıtları çekiyoruz
    cursor.execute("SELECT site, username, password FROM passwords")
    encrypted_passwords = cursor.fetchall()
    con.close()

    if encrypted_passwords:  # Veritabanında herhangi bir kayıt varsa
        print("\n📋 Kayıtlı Şifreler:")
        for site, username, encrypted_password in encrypted_passwords:
            decrypted_password = decrypt_password(encrypted_password)  # Şifreyi çözüyoruz
            print(f"🔹 {site} - Kullanıcı: {username} - Şifre: {decrypted_password}")
    else:
        print("⚠️ Hiçbir şifre kaydı bulunamadı.")
    
def get_password_site(site):
    con = sqlite3.connect(connectString)
    cursor = con.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE site = ?", (site,))
    result = cursor.fetchone()
    con.close()

    if result:
        username, encrypted_password = result  # Şifreyi veritabanından alıyoruz
        decrypted_password = decrypt_password(encrypted_password)  # Şifreyi çözüyoruz
        
        print(f"\n🔎 {site} için giriş bilgileri:")
        print(f"👤 Kullanıcı: {username}")
        print(f"🔑 Şifre: {decrypted_password}")
    else:
        print(f"⚠️ {site} için kayıt bulunamadı.")

def delete_site(site): #kayıt siler
    con=sqlite3.connect(connectString)
    cursor=con.cursor()
    cursor.execute('DELETE from passwords WHERE site = ?',(site,))
    con.commit()
    con.close()
    print(f"🗑️ {site} başarıyla silindi.")

# def add_admin(username,adminpassword):
#     con=sqlite3.connect(connectString)
#     cursor=con.cursor()
#     cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", (username, adminpassword))
#     con.commit()
#     con.close()
#     print(f"✅ {username} için admin kaydı başarıyla kaydedildi.")

# def signAdmin(username, adminpassword):
#     con = sqlite3.connect(connectString)
#     cursor = con.cursor()
    
#     # Kullanıcının şifrelenmiş şifresini veritabanından al
#     cursor.execute("SELECT password FROM admin WHERE username = ?", (username,))
#     result = cursor.fetchone()
#     con.close()

#     if result:
#         encrypted_password = result[0]  # Veritabanındaki şifrelenmiş şifre
#         try:
#             decrypted_password = decrypt_password(encrypted_password)  # Şifreyi çöz

#             if decrypted_password == adminpassword:  # Kullanıcının girdiği şifreyle karşılaştır
#                 return True
#             else:
#                 print("🔴 Hatalı şifre!")
#                 return False
#         except Exception as e:
#             print(f"❌ Şifre çözme hatası: {e}")
#             return False
#     else:
#         print("🔴 Kullanıcı bulunamadı!")
#         return False

