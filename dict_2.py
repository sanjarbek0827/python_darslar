taomlar={
    "Luhmonjon":'Manti',
    'Sanjarbek': 'Dimlama',
    'Sarvarbek':'Mastava',
    'Malikaxon':'osh'
}

# for key, qiymat in taomlar.items():
#     # print(f'{key}, {qiymat}ni  yaxshi kuradi')
#     print(key)
#     print(qiymat)


# Do'kondagi mahsulotlar
# mahsulotlar = { 
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# for masulot in mahsulotlar:
#     print(masulot.capitalize())

#  Umuman olganda keys metodi  ishlatilmaganda  faqat  qiymatlar qaytar ekan
# for masulot in mahsulotlar.keys():
#     print(masulot.capitalize())

mahsulotlar = { 
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
bozorlik = ['anor','uzum','non','baliq']
# for masulot in mahsulotlar:
#     if masulot in bozorlik:
#         print(f'{masulot.capitalize()}  {mahsulotlar[masulot]}  so\'m turadi')
        # ---------------------------------------------------------------------------
    # else:
    #     print(f' quydagi {masulot}lar  mavjud emas')

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f'mana shu {buyum} masulotini  ham qushib oling')




# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.


# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

#  vazifalar -----------------------------------------------------------

# eng_uzb_dict = {
#     "variable": "O'zgaruvchi — ma'lumot saqlaydigan nomlangan joy (masalan: x = 5).",
#     "constant": "O'zgarmas — qiymati o'zgarmaydigan ma'lumot (Python-da konvensiya BARCHA_KATTA_harf).",
#     "data type": "Ma'lumot turi — int, float, str, bool kabi qiymat tiplari.",
#     "int": "Butun son (manfiy yoki musbat, masalan: 7, -2).",
#     "float": "O'nlik son (masalan: 3.14).",
#     "str": "Matn (string) — harflar va belgilar ketma-ketligi.",
#     "bool": "Mantiqiy tip — True yoki False qiymatlar.",
#     "None": "Hech narsa — qiymat yo'qligini bildiradi.",
#     "list": "Ro'yxat — tartiblangan, o'zgartirilishi mumkin bo'lgan elementlar to'plami"
# }

# for lugat in sorted(eng_uzb_dict.items()):
#     print(lugat)





# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

# davlatlar = {
#     "O'zbekiston": "Toshkent",
#     "Qozog'iston": "Ostona",
#     "Qirg'iziston": "Bishkek",
#     "Tojikiston": "Dushanbe",
#     "Turkmaniston": "Ashxobod",
#     "Rossiya": "Moskva",
#     "Xitoy": "Pekin",
#     "AQSH": "Vashington",
#     "Buyuk Britaniya": "London",
#     "Fransiya": "Parij",
#     "Germaniya": "Berlin",
#     "Italiya": "Rim" }

# for Davlat, Poytaxt in sorted(davlatlar.items()):
#     print (f" Davlat : {Davlat}")
#     print(f"Poytaxt : {Poytaxt}")





# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
# bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring

menu = {
    "Osh": 28000,
    "Shashlik": 18000,
    "Manti": 22000,
    "Somsa": 8000,
    "Lag'mon": 25000,
    "Norin": 26000,
    "Chuchvara": 23000,
    "Kabob": 20000,
    "Qovurma lag'mon": 27000,
    "Besh barmoq": 30000,
    "Do'lma": 24000,
    "Salat Olivye": 12000,
    "Palov maxsus": 35000
}


n=int(input("Buyurtmalar soni ----->\n "))
buyurtmalar=[]
jami=0

for i in range(n):
    taom=input(f'{i+1} -taom nomini kirting ').capitalize()
    if taom in menu:
        buyurtmalar.append(taom)
        jami=jami+menu[taom]
        print(f'{taom}  buyrtmalaringizga qushildi {menu[taom]} so\'m')
    else:
        print("Bunday taom mavjud emas ")
for t in buyurtmalar:
    print(f'{t} -> {menu[t]} so\'m turadi')
print(f'Umumiy summa {jami}')