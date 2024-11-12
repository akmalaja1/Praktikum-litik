#Muhammad Akmal Romdhoni
#1C
#2401744

def login():
    
    sandi = "latihan"
    
    chance = 3
    
    print ("selamat datang di menu login")

    for i in range (chance):
        username = input("masukkan username: ")
       
        password = input(f"kesempatan {i+1}/{chance} - masukkan password: ")
        
        if password == sandi:
            print("nah bener, login berhasil cihuy")
            return
        else:
            if i == chance - 1:
                print("Kesempatan Anda sudah habis, Anda akan keluar dari sistem.")
        
            else:
                print("password salah, silahkan coba lagi")
    
login()