#Muhammad Akmal Romdhoni
#1C
#2401744

def hitung_selisih():
    jam_mulai = int(input("inputkan jam mulai: "))
    menit_mulai = int(input("inputkan menit mulai: "))
    detik_mulai = int(input("inputkan detik mulai: "))
    
    jam_selesai = int(input("inputkan jam selesai: "))
    menit_selesai = int(input("inputkan menit selesai: "))
    detik_selesai = int(input("inputkan detik selesai: "))
    
    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai *60 + detik_selesai
    selisih_detik = total_detik_selesai - total_detik_mulai
    
    jam = selisih_detik//3600
    menit = (selisih_detik%3600)//60
    detik = selisih_detik%60
    
    print(f"Selisih: {jam}jam - {menit}menit - {detik}detik")
    
hitung_selisih()