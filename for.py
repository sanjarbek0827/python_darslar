# mehmonlar=[" \t Ali","Vali","Jamshid","Bobur",'Alimardon','Salohiddin']
# for mehmon in mehmonlar :
#     print(f'  Asslaslomu aleykum  Hurmatli  {mehmon}.\nSizni bugungi tadbirimizga tashrif buyurishingizni suraman')



# sonlar=list(range(1,11))
# sonlar_kvadrati=[]
# for i in sonlar:
#     sonlar_kvadrati.append(i**2)
#     print(sonlar)
#     print(sonlar_kvadrati)
# shu holda bulsa  forni ichida bulsa print sikil davom etib qayta chiqaraveradi
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 4]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 4, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 4, 9, 16]  davomiy ravishda

#  tugrisi quydagi shakilda buladi
# sonlar=(list(range(1,11)))
# sonlar_kvadrati=[]
# for i in sonlar:
#     sonlar_kvadrati.append(i**2)
# print(sonlar)
# print(sonlar_kvadrati)
# va natija quydagi 
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# oila=[]
# print("Siz eng yaqin oila azolaringizni kimlar? ")
# for  i in range(4):
#     oila.append(input(f"{i+1}  Assalomu aleykum "))
# print(oila)


#  #Vazifa  
# # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

# ismlar=['Sanjarbek','Og\'abek','Jovohir', 'Jamshid','Bobur']
# for ism in ismlar:
#     print(f'Assalomu aleykum {ism}')
# # Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print(f'Kod {len(ism)} marta takrorlandi')


#  10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

# kubi=[]
# for i  in range(100):
#     kubi.append(f'{i+1} soning kubi quydaginga teng {(i+1)**3}')
# print(kubi,)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

# kinolar=[]
# print("Sizning sevimli kinolarini kiring")
# for kino in (range(5)):
#     # print(f"{kino+1}-Sizning sevimli kinolarini kiring")
#     kinolar.append(input(f'  {kino+1}-sevilmi kino nomini kriting  '))
# print(kinolar)


# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va
#  har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

# suhbatdosh=[]
# n=int(input("Nechta marta takrorlansin: "))
# print('Suhbatlashgan insonlaringizni  birma bir kirting ')
# for suhbat in range(0,n):
#     suhbatdosh.append(input(f"{suhbat+1} insongizni ismini kirting  "))
# print(suhbatdosh)
