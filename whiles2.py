# print("Yaqin  dustlar ruyhatini yatyapsiz!")
# dustlar=[]
# n=1
# while True:
#     savol=(f'{n} dustingiz kiritinng>>>  ' )
#     ism=input(savol)
#     dustlar.append(ism)
#     takror=input(f'Yaqin dustlaringiz kirtishngizni davom etirasizmi?  ha/yo\'q ->  ')
#     n+=1
#     if takror!='ha':
#         break
# print('Yaqin dustlarnigiz ruyhati')
# for ism in dustlar:
#     print(f'{ism.title()}')



# print("Dustlarnigiz yoshini saqlaymiz ")
# dustlar={}
# ishora=True
# while ishora:
#     ism=input(f'Dustlaringiz ismini kirting>>> ')
#     yosh=input(f'{ism.capitalize()}ni yoshini kirting -> ')
#     dustlar[ism.title()]=int(yosh)
#     javob=input('Yana malumot kirtasizmi? ha/yo\'q -> ')
#     if javob=='yo\'q':
#         ishora=False
# for ism,yosh in dustlar.items():
#     print(f'{ism.capitalize()} {yosh} yoshda ')
# print(dustlar)


cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
car='nexia'
# while car in cars:
#     cars.remove(car)
# print(cars)


# talabalar = ['hasan', 'husan', 'olim', 'botir']

# b_talablar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f'{talaba.capitalize()} ni baholang-> ')
#     print(f"{talaba.capitalize()} baholandi")
#     b_talablar[talaba.title()]=int(baho)
# print(b_talablar.keys[talaba.title()])





# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# print('Mahsulot nomini qaytaruvchi dastur')
# savol=("Masulot nomini kirting->  ")
# maxsulotlar=[]
# while True:
#     maxsulot=input(savol)
#     maxsulotlar.append(maxsulot.title())
#     javob=input('yana maxsulotni kirtishni hohlaysizmi? ha/yo\'q  ')
#     if javob!='ha':
#         break
# print(maxsulotlar)
    
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.


# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
# while buyurtmalar:
#     buyurtma=buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh=mahsulotlar[buyurtma]
#         print(f'{buyurtma.title()} narxi {narh} so\'m ')
#     else:
#         print('Bunday buyurtma yo\'q')




# Foydalanuvchi sonlar kiritaversin. 0 kiritsa sikl to‘xtasin. Sonlarni ro‘yxatga yig‘ing, keyin:
# eng katta son
# eng kichik son
# o‘rtacha qiymat
# ni chiqaring.


# from statistics import mean
# print("Sonlarni qaytaruvchi dastur ")

# savol='Son kirting '
# savol+=('Skilni tuxtatmoqchi bulsangiz 0 nikirting ')
# sonlar=[]
# ishora=True
# while ishora:
#     son=input(savol)
#     sonlar.append(son)
#     son=int(son)
#     if son==0:
#         ishora=False
# print(sonlar)
# for son in sonlar:
#     son1=max(sonlar)
#     son2=min(sonlar)
#     son3=mean(sonlar)
# print(f'sonning eng kattasi  {son1} \n eng kichik son {son2} \n o\'rtacha qiymati  {son3} ')


# While orqali foydalanuvchidan mahsulot nomi va narxini so‘rang. stop deb yozilganda tugasin. Hammasini lug‘atda saqlang.


# bozorlik={}

# while True:
#     qiymat=input("maxsulot nomini kirting ( Tuxtatish uchun stop kiting)- >  ")

#     if qiymat=='stop':
#         break 

#     narx=input('maxsulotni narxini kirting->  ')
#     bozorlik[qiymat.title()]=int(narx)

    

# for qiymat,narx in bozorlik.items():
#     print(f'{qiymat}ning narxi {narx} da')

# print(bozorlik)


# Foydalanuvchi do‘stlarining ismlarini while orqali kiritsin. Keyin ro‘yxatdagi ismlarni lug‘atga (ism: uzunligi) aylantiring.
dustlar1={}
while True:
    ism=input('Ismi kirting -> ')
    javob=input("davom etirishni hohlaysizmi ? ha/yo\'q-> ")
    dustlar1[ism.capitalize()]=len(ism)
    
    if javob== 'yo\'q':
        break
    
for ism ,uz in dustlar1.items():
    print(f'{ism} uzunligi {uz} ga teng')
print(dustlar1)