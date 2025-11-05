# cars={'model':'Laseti','rang':'mokriy'}
# print(f'{cars["model"]} \n{cars["rang"]} ')

mevalar={'olma':1000,'nok':2000, 'shaftoli':2100,}
# print(f"nokning kilosi {mevalar['nok']} sumdan")

# talaba={'ismi':'sanjarbek Junaydullayev','yosh':22, 'tugilgan_y':2003}
# print(f"Mening ismim {talaba['ismi'].title()}, yoshim {talaba['yosh']} da, tugilgan {talaba['tugilgan_y']}-yil")
# talaba['kursi']= 4
# talaba['fakulteti']="Tff"
# talaba['ismi']='johon'
# print(talaba)

#  bu yerda  bush lugatga  malumotlar qushish musuli
talaba_1={}
talaba_1['ism']='Johonbek'
talaba_1['t_yili']=2004
talaba_1['kurs']=4
talaba_1['fakulteti']='TTF'

# del talaba_1['t_yili'] 
# print(f"Mening ismim {talaba_1['ism']} tugilgan yilim {talaba_1['t_yili']}  fakutetim {talaba_1['fakulteti']} ning  {talaba_1['kurs']}-kurs talabasiman")
yangi_talaba=talaba_1.copy()
yangi_talaba['familya']='Dusmurodov'
yangi_talaba['t_joyi']='Samarqand'
# print(yangi_talaba)
print(talaba_1) 

# if talaba_1.get('ism')=='Johonbek':
#    print(f'mening  ismim {talaba_1.get('ism')}')
# else:
#    print("Bunday ismli talab yuq")

