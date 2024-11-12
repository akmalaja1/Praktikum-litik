#Muhammad Akmal Romdhoni
#1C
#2401744

import math 

def volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari ** 2 * tinggi
    return volume

#misal

jari_jari = 7

tinggi = 7

volume = volume_tabung(jari_jari, tinggi)

print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume: .2f}")