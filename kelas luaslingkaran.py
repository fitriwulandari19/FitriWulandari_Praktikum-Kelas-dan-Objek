class LuasLingkaran(object):
    def __init__(self, phi, r):
        self.phi = phi
        self.jarijari = r
    def hitungLuas(self):
        return self.phi * self.jarijari**2
    
def main():
    luaslingkaran1 = LuasLingkaran(3.14, 3)

    print('Objek luaslingkaran1')
    print('phi\t        : ', luaslingkaran1.phi)
    print('jari-jari\t: ', luaslingkaran1.jarijari)
    print('luas\t= ', luaslingkaran1.hitungLuas())
   

    luaslingkaran2 = LuasLingkaran(3.14, 6)

    print("\nObjek luaslingkaran2")
    print("phi\t        : ", luaslingkaran2.phi)
    print("jari-jari\t: ", luaslingkaran2.jarijari)
    print("luas\t= ", luaslingkaran2.hitungLuas())

if __name__ == "__main__":
    main()
