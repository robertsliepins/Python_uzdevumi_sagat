"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) kadus ciparus jus zinat? Arabu
2) kadus romiesu ciparus zinat? I V C X M L D
3) kas ir klase? klase ir prohrammesans struktura kas var defininet datu uzvedibu un metodes
4) klase sastav no konstruktora/destruktora un metodem(iekšejam funkcijam)

 parametri () ir iekseji klases mainigie
 kadas datu strukturas zinu? 
 -list (saraksts) a=""
 -arry (masivs)
 -dict (vardnica) a-{} a=dict()

5) vardnica var saprast ka tabulu ar divam kolonam

"""
class AAA:
    # jadefine konstruktors
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
    # define metodes
    def to_roman(self,num):
        result= ""
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x:x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
    #num=num- value
        return result
    
#pimers
skaitlis=2023
#define objektu
kk=AAA()
#jaunajam obkektam jaizsauc klases metode
romieshu=kk.to_roman(skaitlis)

#noformet izdruku
print(f"{skaitlis} ar romieshu cipariem ir {romieshu}")