info = "ini di dalam modul sapa import"


def sapa_nama(nama):
    print(f"halo {nama}")


print(__name__)


if __name__ == "__main__":
    print("Ini di dalam modul sapa kalau sapa name=main, file sapa sebagai modul utama")
