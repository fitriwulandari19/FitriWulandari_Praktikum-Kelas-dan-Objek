class KelilingLingkaran(object):
    def __init__(self, phi, r):
        self.phi = phi
        self.jarijari = r
    def hitungKeliling(self):
        return 2*self.phi * self.jarijari

def main():
    kelilinglingkaran1 = KelilingLingkaran(3.14, 6)

    print('Objek Kelilinglingkaran1')
    print('phi\t        : ', kelilinglingkaran1.phi)
    print('jari-jari\t: ', kelilinglingkaran1.jarijari)
    print('keliling\t= ', kelilinglingkaran1.hitungKeliling())
   

    kelilinglingkaran2 = KelilingLingkaran(3.14, 3)

    print("\nObjek kelilinglingkaran2")
    print("phi\t        : ", kelilinglingkaran2.phi)
    print("jari-jari\t: ", kelilinglingkaran2.jarijari)
    print("keliling\t= ", kelilinglingkaran2.hitungKeliling())

if __name__ == "__main__":
    main()

