import sys
import os
from db import initialize_db, add_site, get_all_password, get_password_site, delete_site
from encryption import encrypt_password
from createpassword import generate_random_pw

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\n"
    "█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀█\n"
    "█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █▀▄\n"
    "-------------------------------------------------------------\n"
    "[1] Yeni Kayıt Ekle  [2] Belirli Bir Site İçin Şifre Göster\n"
    "[3] Tüm Şifreleri Göster  [4] Kayıt Sil  [5] Çıkış\n"
    "-------------------------------------------------------------"
    )

def main():
    initialize_db()
    while True:
        show_menu()
        choice = input('🔹 Seçiminizi Yapın: ')

        if choice == '1':
            site = input('🔹 Site ismi: ')
            username = input('🔹 Kullanıcı Adı: ')
            print('🔹 Güvenli şifre oluşturmak için [random] yazın.')
            password = input('🔹 Şifre: ')
            
            if password.lower() == 'random':
                password = generate_random_pw()
                print(f'✅ Oluşturulan Şifreniz: {password}')

            encrypted_password = encrypt_password(password)
            add_site(site, username, encrypted_password)
            print('✅ Şifre başarıyla kaydedildi!')

        elif choice == '2':
            site = input("🔹 Site Adı: ")
            get_password_site(site)

        elif choice == '3':
            get_all_password()

        elif choice == '4':
            site = input('🔹 Silinecek Site İsmi: ')
            delete_site(site)
            print('✅ Kayıt başarıyla silindi!')

        elif choice == '5':
            print("👋 Çıkış yapılıyor...")
            sys.exit()

        else:
            print("⚠️ Geçersiz seçenek! Lütfen tekrar deneyin.")

        input('\n🔹 Devam etmek için bir tuşa basın...')
        clear_console()

if __name__ == "__main__":
    main()
