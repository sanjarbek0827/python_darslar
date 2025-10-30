# Raqamli ball	Harf darajasi
# 90 <= ball <= 100	'A'
# 80 <= ball < 90	"B"
# 70 <= ball < 80	'C'
# 60 <= ball < 70	'D'
# 0 <= ball < 60	"F"
# Tekshirilgan qiymatlarning barchasi 0 dan 100 gacha. Salbiy qiymatlar yoki 100 dan katta qiymatlarni tekshirishning hojati yo'q.

# ball=int(input('Ballni kirting va ular quydagi sonlarni oraligida bulsin 60 va 100 \n>>>'))
# if 90<= ball<=100:
#     print('A')
# elif 80<= ball<90:
#     print("B")
# elif 70 <= ball < 80:
#     print('C')
# elif 60 <= ball < 70:
#     print('D')
# elif 0 <= ball < 60:
#     print("F")
# else:
#     print("yuqoridagi sonlar oralr oraligida bulishi kerak")



# Natan velosiped haydashni yaxshi ko'radi.
# Neytan suvsizlanish muhimligini bilganligi sababli, velosipedda bir soatda 0,5 litr suv ichadi.
# Sizga soatlab vaqt beriladi va siz Neytan ichadigan litr sonini qaytarishingiz kerak, yaxlitlangan .

import math
time=float(input("Vaqtni kirting  "))
qiymat=math.floor(time*0.5)
print(f"Neyton ichidagan suv miqdori    {qiymat}")