class LuasLingkaran(object):
    def __init__(self, phi, r):
        self.phi = phi
        self.jarijari = r
    def hitungLuas(self):
        return self.phi * self.jarijari**2
    def cetakData(self):
        print("phi\t        : ", self.phi)
        print("jari-jari\t: ", self.jarijari)
    def cetakLuas(self):
        print("LuasLingkaran\t= ", self.hitungLuas())

def main():
    luaslingkaran1 = LuasLingkaran(3.14, 6)

    print("Objek luaslingkaran1")
    luaslingkaran1.cetakData()
    luaslingkaran1.cetakLuas()

    luaslingkaran2 = LuasLingkaran(3.14, 3)
    print("\nObjek luaslingkaran2")
    luaslingkaran2.cetakData()
    luaslingkaran2.cetakLuas()

if __name__ == "__main__":
    main()
