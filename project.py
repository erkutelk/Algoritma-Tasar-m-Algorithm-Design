# 
class Mains:
    ikidenBuyukSayac = []
    def __init__(self, sayilar) -> None:
        self.sayilar = sayilar
        self.sayac=0
    def ikidenBuyuk(self):
        for a in self.sayilar:
            if a > 2:
                Mains.ikidenBuyukSayac.append(a)
                
    def ardardaGelenDeger(self):
        for a in range(len(self.sayilar)-1):
            if self.sayilar[a]>=2 and self.sayilar[a+1]>=2:
                print('Bu iki sayı ikiden büyük\t>',self.sayac)
                self.sayacReset()
                # Her iki sayı ikiden büyük ise sayacı sıfırlamamız gerekiyor

            else:
                print('Bu iki sayı ikiden küçük\t>',self.sayac)
                self.sayac+=1
                
    def sayacReset(self):
        self.sayac=0
            
            

deger = [1,2, 1.3, 1.3, 4, 5, 6, 7, 8, 9, 10,1.2,1.3,1.1,0,1]
ornek = Mains(deger)
ornek.ikidenBuyuk()
ornek.ardardaGelenDeger()
