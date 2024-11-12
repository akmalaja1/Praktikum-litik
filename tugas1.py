#Muhammad Akmal Romdhoni
#1C
#2401744


def fibonacci(n):

    deret = [0,1]
    for i in range(2,n):
        deret.append(deret[i-1] + deret[i-2])
    return deret
    
User = int(input("Masukkan banyak bilangan fibonacci yg mau di tampilkan: "))
if User>0:
    hasil = fibonacci(User)
    print("deret fibonacci sebanyak", User, "adalah", hasil)   
else:
    print("Masukkan bilangan positif!!!")     