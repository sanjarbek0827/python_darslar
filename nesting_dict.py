car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
cars=[car0,car1,car2]
# for car in cars:
#     print(car)

# print(f"{cars[1] ['model'].title()}\
# print(f"{cars[0] ['yil']} \n"
#       f'{cars[0] ['korobka'].title()}')



# malubus=[]
# for n in range(10):
#     new_car={
#         'model':'malubu',
#         'rang':None,
#         'yili':2021,
#         'narh':None,
#         'km':0,
#         'korobka':'avtomat'
#     }
#     malubus.append(new_car)
# for malubu in malubus [:4]:
#     malubu['rang']='qizil'

# for malubu  in malubus [4:8]:
#     malubu['rang']='yashil'
#     malubu['korobka']='mehanika'

# for malubu  in malubus [8:10]:
#     malubu['rang']='oq'

# for malubu in malubus:
#     if malubu['korobka']=='avtomat':
#         malubu['narh']=40000
#     else:
#         malubu['narh']=30000

# for malubu in malubus:
    # print(malubu)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()}  quydagi dasturlash tilini biladi")
#     for til in tillar:
#         print(til.upper(), end='  ')


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} , {info['familiya'].title()} tugilgan yili {info['tyil']} malumoti {info['malumot']}\n"
#           f"  U quydai dasturlsh tillarini biladi >>>",end=" ")
#     for til in info['tillar']:
#         print(til.upper() ,end="  ")




# <<<             Vazifalr             >>

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

mashhur_shaxslar = {
    "Alisher Navoiy": {
        "turi": "Adabiyot arbobi",
        "davri": "XV asr",
        "mashhur_asarlari": ["Xamsa", "Lison ut-Tayr", "Mahbub ul-qulub"],
        "qisqacha_haqida": "Alisher Navoiy o‘zbek adabiyotining asoschisi, shoir, davlat arbobi va mutafakkir bo‘lgan."
    },

    "Abdulla Qodiriy": {
        "turi": "Adib",
        "davri": "XX asr boshlarida yashagan",
        "mashhur_asarlari": ["O‘tkan kunlar", "Mehrobdan chayon"],
        "qisqacha_haqida": "Abdulla Qodiriy o‘zbek romanchiligining asoschisi bo‘lib, o‘z asarlari orqali milliy ongni yuksaltirgan."
    },

    "Elon Musk": {
        "turi": "Texnologiya tadbirkori",
        "davri": "Zamonaviy davr",
        "kompaniyalari": ["Tesla", "SpaceX", "Neuralink", "X (Twitter)"],
        "qisqacha_haqida": "Elon Musk — elektr avtomobillar, kosmik parvozlar va sun’iy intellekt sohalarida inqilob qilgan tadbirkor."
    },

    "Mark Zuckerberg": {
        "turi": "Internet tadbirkori",
        "davri": "Zamonaviy davr",
        "kompaniyalari": ["Meta (Facebook)", "Instagram", "WhatsApp"],
        "qisqacha_haqida": "Mark Zuckerberg — Facebook asoschisi bo‘lib, dunyo miqyosida ijtimoiy tarmoqlar rivojiga katta hissa qo‘shgan."
    }
}

# for ism , info in mashhur_shaxslar.items():
#     print(f"\n {ism}  quydagi sanat turi bilan shugilangan  {info['turi']}"
#           f' yashagan davri {info['davri']}   asarlari  {info.get('mashhur_asarlari')}  yoki kompanyalari  {info.get("kompaniyalari")}'
#           f' uzi haqida qisqacha malumoti {info['qisqacha_haqida']}')



# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

# for ism,kinolar in kinolar.items():
#     print(f'{ism.capitalize()}  va uning yoqtirgan kinolarni quydagilar')
#     for kino in kinolar:
#         print(kino.upper())

