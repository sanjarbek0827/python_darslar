# avtolar=['Chevrolet','Audi','Bmw','volvo','kia','huyundai']
# for avto in avtolar:
#     if  avto=='Bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())



# ism=input("Ismingiz nima?\n>>>  ")
# if ism.lower() !='sanjarbek':
#     print(f'Uzur {ism.title()} biz Sanjarbekni kutyapmiz')
# else:
#     print("Salom Sanjarbek")

# Ro'yxatdagi elementlar sonini hisoblang
# # print(len(sonlar))


# sonlar=[1, -4, 7, 12]
# musbat=[]
# for son in sonlar:
#     if son >0:
#         musbat.append(son)
#     else:
#         print(f'Bu {son} odan katta emas ')

# print(f'{sonlar[0]}+{sonlar[2]}+{sonlar[3]}={sum(musbat)}')



# print("Login malumotingizni kirting")
# login=input('login malumotingi kamida 5 tadan kup bulishi kerak\n >>>>>>  ')
# if len(login)<=5:
#     print(f'{login} xatolik  bor')
# else:
#     print("siz kirtigan login tugri ")


# yil=int(input("tugilgan yilingizni kiriting  "))
# if 2025-yil<18:
#     print(f'Sizning yoshingiz{2025-yil} dan kichik mukin emas')
# else:
#     print(f"Sizning yoshingiz {2025-yil}  da ruhsat etiladi")





# vazifalar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=="gm":
#         print(car.upper())
#     else:
#         print(car.title())

# Yuqoridagi mashqni teng emas ( !=) operatori yordamida teng bajaring.

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car !="gm":
#         print(car.upper())
#     else:
#         print(car.title())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

# login=str(input("loginni kirting \n>>>   "))
# if login.lower()=="admin":
#     print(f'Xush kelibsz, Admin')
# else:
#     print(f"Xush kelibsiz, {login} siz admin xuquqiga ega emassiz!")




# foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring


# son=float(input('marhamat soni kirting '))
# if son%2==0 and son>0:
#     print("Bu son  juft ")
# elif son%2!=0  and son>0:
#     print("toq son")
# else:
#     print("Bu son na toq son na juft")



# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm



# yosh=int(input("Yoshingizni kirting  "))
# if 60<yosh<4 and yosh>0:
#     print("MArhamat siz bepulga kirishingiz mumkin")
# elif 0<yosh<18:
#     print("Sizga beriladigan chipta narxi 10,000")
# elif yosh>20:
#     print("Sizga beriladigan chipta narxi 20,000")
# else:
#     print("Hecha narsa kirtmadingiz")



# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat 
# yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar 
# ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda
# yo'q" degan xabarlarni chiqaring





# from colorama import Fore
# mahsulotlar=['olma','nok','gilos','shaftoli','urik','karam','sabzi']
# savat=[]
# for n in range(5):
#     savat.append(input(f'Savatga {n+1} - mahsulot qushing   '))


# for mahsulot in savat:
#     if not mahsulot in mahsulotlar:
#         print(f"Savatimizda  {mahsulot}  yoq")
        
#     else:
#         print(f"Savatimizda { mahsulot}  bor")

# for mahsulot in savat:
#     savat.remove(mahsulot)
#     print(Fore.RED+mahsulot +Fore.WHITE)
# print(savat)



# menyu=['osh','somsa','shashlik','mastava','lagmon']
# buyurtmalar=['somsa0','lagmon','manti','shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menyu:
#             print (f'Menyuda {taom} bor')
#         else:
#             print(f'Bunday { taom} menyuda yoq')
# else:
#     print(f'Savatchangiz bush')



# sonlar=input("Sonlarni kiritng  " )
# yangi_son=[]
# for  son in sonlar.split():
#     yangi_son.append(int(son))

# yigindi=0
# for son in yangi_son:
#     yigindi=yigindi+son**2

# print(f'KAvadratlarni yigindis {yigindi}')




# sonlar=input("Sonlarni kiritng  " )
# yangi_son=[]
# for  son in sonlar.split():
#     yangi_son.append(float(son))
# yigindi=0
# for son in yangi_son:
#     yigindi=yigindi+son







# list1=[34, 15, 88, 2]
# list2=[34, -345, -1, 100]
# print(f'brinchi listdan en kichik son  {min(list1)} \nikkinchi listdan eng kichik son {min(list2)} ')







# 1 dan songacha bo'lgan har bir sonning yig'indisini topadigan dastur yozing (ikkalasi ham kiradi). Raqam har doim 0 dan 
# katta musbat butun son bo'ladi. Sizning funksiyangiz faqat natijani qaytarishi kerak, quyidagi misolda qavslar orasida 
# ko'rsatilgan narsa bu natijaga qanday erishishingiz va bu uning bir qismi emas, namunali testlarga qarang.


# son=int(input("Musbat sonlar kirting  "))
# yigindi=(son*(son+1))//2

# print(f'1 dan  {son} sonlar yigindisi {yigindi}')



















