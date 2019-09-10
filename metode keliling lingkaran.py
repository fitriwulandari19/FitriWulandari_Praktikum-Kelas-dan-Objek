class KelilingLingkaran(object):
    def __init__(self, phi, r):
        self.phi = phi
        self.jarijari = r
    def hitungKeliling(self):
        return 2*self.phi * self.jarijari
    def cetakData(self):
        print("phi\t        : ", self.phi)
        print("jari-jari\t: ", self.jarijari)
    def cetakKeliling(self):
        print("KelilingLingkaran\t= ", self.hitungKeliling())

def main():
    kelilinglingkaran1 = KelilingLingkaran(3.14, 6)

    print("Objek kelilinglingkaran1")
    kelilinglingkaran1.cetakData()
    kelilinglingkaran1.cetakKeliling()

    kelilinglingkaran2 = KelilingLingkaran(3.14, 3)
    print("\nObjek kelilinglingkaran1")
    kelilinglingkaran2.cetakData()
    kelilinglingkaran2.cetakKeliling()

if __name__ == "__main__":
    main()
