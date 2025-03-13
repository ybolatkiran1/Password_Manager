import os
from cryptography.fernet import Fernet

# 📌 Şifreleme anahtarını oluşturup kaydet
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# 📌 Mevcut anahtarı yükleyen fonksiyon (Eğer yoksa oluşturur)
def load_or_create_key():
    if not os.path.exists("key.key"):
        print("🟡 Anahtar dosyası bulunamadı, yeni anahtar oluşturuluyor...")
        generate_key()
    
    with open("key.key", "rb") as key_file:
        return key_file.read()

# 📌 Anahtarı yükle veya oluştur
key = load_or_create_key()
cipher = Fernet(key)

# 📌 Şifreleme fonksiyonu
def encrypt_password(password: str) -> bytes:
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password

# 📌 Şifre çözme fonksiyonu
def decrypt_password(encrypted_password: bytes) -> str:
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password
