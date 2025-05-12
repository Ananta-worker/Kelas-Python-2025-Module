"""
Pengenalan Module
* Module adalah file python yang berisi kumpulan kode python (kelas/fungsi/variable), file python ini memiliki ekstensi
 .py (nama_module.py)
* Package adalah kumpulan dari module-module python dengan tujuan tertentu.
* Kita juga dapat membuat module kita sendiri dengan mengetikkan variable atau fungsi atau kelas di dalam file python.
* Kemudian kita dapat menggunakan module tersebut di kode python yang lain.
"""
import sapa
from aritmatika import penjumlahan, pengurangan, perkalian, pembagian

print(sapa.info)
sapa.sapa_nama("Andii")

penjumlahan(8, 12)
pengurangan(8, 12)
perkalian(8, 12)
pembagian(8, 12)

print(__name__)
print(__doc__)
print(__file__)

if __name__ == "__main__":
    print('\nModule "membuat_module" sebagai modul utama/main module')
