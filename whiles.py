

# ism=input('Ismingizni kirting  ')
# savol=f'Salom {ism.title()}. Yoshiingiz Nechida ?  '
# yosh=input(savol)
# yosh= int(yosh)
# hegiht= input("bo\'yingiz nechi metr  ")
# hegiht=float(hegiht)


# son=1
# while son<=5:
#     print(son, end=',')
#     son+=1
# print("dastur yakunlandi")

# print("Kirtgan songizni  kvadratga oshirib qaytaruvchi dastur")
savol=("Istalgan savomni kirting ")
savol+=("dasturni  tugatmoqchi bulsangiz 'exit' suzini kirting>>> ")
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)
# print('dastur tugadi')


# Ishora (flag)

# Bunday holatlarda biror o'zgaruvchidan ishora (flag) sifatida foydalanishimiz mumkin. 
# Agar dastur bajarilishi davomida dasturni to'xtatish shartlaridan biri bajarilganda ,
# ishora o'zgaruvchining qiymatini o'zgartiramiz va dastur o'z-o'zidan to'xtaydi

# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)


# BREAK OPERATORI
# Break operatori yordamida ma'lum bir shartni tekshirish va whiletsikli bajarilishini to'xtatib qo'yish mumkin.


# while True:  # abadiy tsikl
#     qiymat=input(savol)
#     if qiymat=='exit':
#         print("dastur yakunlandi")
#         break

#     else:
#          print(float(qiymat)**2)
    




# Break operatori fortsiklini to'xtatish uchun ham ishlatiladi.

# sonlar=list(range(1,10))
# for son in sonlar:
#     if son==5:
#         break
#     print(f'{son} sonning kvadrati {son**2} ga teng')





# CONTINUE OPERATORI
# Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan.
    
    
# sonlar=list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     print(f'{son} sonning kvadrati {son**2} ga teng')







# vazifalar 




# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating


# savol=("siz yoqtirgan kitobingizni kirting ")
# savol+='(Barcha kitoblarni kirtib berganingizdan so\'ng   " stop " suzini kirting)   '
# while True:
#     kitob=input(savol)
#     if kitob=='stop':
#         print("Dastur yakunlandi")
#         break
# print(f'Rahmat  {kitob}')




# savol="Yoshingizni kirting "
# while True:
#     qiymat=input(savol)
#     if qiymat=='exit' or qiymat=='quit':
#         break
#     yosh=int(qiymat)

#     if 0<yosh<=7:
#         narh=2000
#     elif 7< yosh <= 18:
#         narh=5000
#     elif 19<= yosh<=65:
#         narh=10000
#     else:
#         narh=0
#     if narh==0:
#         print("sizga chipta tekin")
#     else:
#         print(f'chipta narxi{narh}')
# print("dastur yakunlandi")













# savol="Yoshingizni kirting "
# ishora=True
# while ishora:
#     qiymat=input(savol)

#     if qiymat=='exit' or qiymat=='quit':
#         ishora=False
#         continue
#     yosh=int(qiymat)


#     if 0<yosh<=7:
#         narh=2000

#     elif 7< yosh <= 18:
#         narh=5000

#     elif 19<= yosh<=65:
#         narh=10000
        
#     else:
#         narh=0

#     if narh==0:
#         print("sizga chipta tekin")

#     else:
#         print(f'chipta narxi{narh}')


# print("dastur yakunlandi")








# savol="Yoshingizni kirting "
# qiymat=''
# while qiymat=='exit' or 'quit':
#     qiymat=input(savol)
#     if qiymat=='exit' or qiymat=='quit':
#        break
#     yosh=int(qiymat)
   


#     if 0<yosh<=7:
#         narh=2000

#     elif 7< yosh <= 18:
#         narh=5000

#     elif 19<= yosh<=65:
#         narh=10000
        
#     else:
#         narh=0

#     if narh==0:
#         print("sizga chipta tekin")

#     else:
#         print(f'chipta narxi{narh}')


# print("dastur yakunlandi")

 


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


 




















































