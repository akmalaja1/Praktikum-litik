
#Muhammad Akmal Romdhoni
#1C
#2401744

def hitung_total_dan_rata_rata():
    total = 0     
    count = 0     

    print("Masukkan nilai satu per satu. Ketik 0 untuk selesai: .")

    while True:
        input_nilai = input("Masukkan nilai: ")

        if input_nilai == "0":
            break  
        
        if input_nilai:
            angka = int(input_nilai)
            total += angka    
            count += 1       
        else:
            print("masukin angka yg bener")
              
    if count > 0:
        rata_rata = total / count  
    else:
        rata_rata = 0              

    return total, rata_rata


total, rata_rata = hitung_total_dan_rata_rata()


print(f"Total: {total}")
print(f"Rata-rata: {rata_rata}")
