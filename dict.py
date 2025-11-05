# cars={'model':'Laseti','rang':'mokriy'}
# print(f'{cars["model"]} \n{cars["rang"]} ')

# mevalar={'olma':1000,'nok':2000, 'shaftoli':2100,}
# print(f"nokning kilosi {mevalar['nok']} sumdan")

# talaba={'ismi':'sanjarbek Junaydullayev','yosh':22, 'tugilgan_y':2003}
# print(f"Mening ismim {talaba['ismi'].title()}, yoshim {talaba['yosh']} da, tugilgan {talaba['tugilgan_y']}-yil")
# talaba['kursi']= 4
# talaba['fakulteti']="Tff"
# talaba['ismi']='johon'
# print(talaba)

#  bu yerda  bush lugatga  malumotlar qushish musuli
# talaba_1={}
# talaba_1['ism']='Johonbek'
# talaba_1['t_yili']=2004
# talaba_1['kurs']=4
# talaba_1['fakulteti']='TTF'
# print(talaba_1.clear())

# del talaba_1['t_yili'] 
# print(f"Mening ismim {talaba_1['ism']} tugilgan yilim {talaba_1['t_yili']} \
#  fakutetim {talaba_1['fakulteti']} ning  {talaba_1['kurs']}-kurs talabasiman")
# yangi_talaba=talaba_1.copy()
# yangi_talaba['familya']='Dusmurodov'
# yangi_talaba['t_joyi']='Samarqand'
# # print(yangi_talaba)
# print(talaba_1) 

# if talaba_1.get('ism')=='Johonbek':
#    print(f'mening  ismim {talaba_1.get('ism')}')
# else:
#    print("Bunday ismli talab yuq")










# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring:


# from colorama import Fore,Back
# otam={"ismi":'Mirzayev Ilhomjon Junaydullayevich', 't_yili': 1983, 't_joyi':'Namangan viloyati Chortoq tumani'}
# onam={"ismi":'Mirzayeva Nafisa Alijonovna','t_yili': 1983, 't_joyi':'Namangan viloyati Chortoq tumani'}
# singlim={'simi ':'Junaydullayeva Mahliyo Ilhomjon qizi','t_yili': 2009, 't_joyi':'Namangan viloyati Chortoq tumani'}
# print( Fore.GREEN+f" Mening  otam {otam ['ismi']}, {otam['t_yili']}-yi; , {otam ["t_joyi"]} da tugilgan \
# \n {Fore.BLUE}Mening onam {onam['ismi']}, {onam['t_yili']}-yil, {onam['t_joyi']} da tavallud topganlar \
# \n { Fore.RED}Mening  singlim {singlim['simi ']} , {singlim['t_yili']}- yil, {singlim['t_joyi']} da tugulgan {Back.BLACK}" )




# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# taomlar={
#     "Luhmonjon":'Manti',
#     'Sanjarbek': 'Dimlama',
#     'Sarvarbek':'Mastava',
#     'Malikaxon':'osh'
# }
# taom=taomlar['Malikaxon']

# print(f' Malikaxon {taom} ni juda yaxsi kuradi')




# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

eng_uzb_dict = {
    "variable": "O'zgaruvchi — ma'lumot saqlaydigan nomlangan joy (masalan: x = 5).",
    "constant": "O'zgarmas — qiymati o'zgarmaydigan ma'lumot (Python-da konvensiya BARCHA_KATTA_harf).",
    "data type": "Ma'lumot turi — int, float, str, bool kabi qiymat tiplari.",
    "int": "Butun son (manfiy yoki musbat, masalan: 7, -2).",
    "float": "O'nlik son (masalan: 3.14).",
    "str": "Matn (string) — harflar va belgilar ketma-ketligi.",
    "bool": "Mantiqiy tip — True yoki False qiymatlar.",
    "None": "Hech narsa — qiymat yo'qligini bildiradi.",
    "list": "Ro'yxat — tartiblangan, o'zgartirilishi mumkin bo'lgan elementlar to'plami"
}
tarjima=input("Suz kirting ")
if tarjima in eng_uzb_dict:
    print(f"{tarjima}---> {eng_uzb_dict [tarjima]}")
else:
    print("bunday suz mavjud emas")







 











