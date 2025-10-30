# list ruyhati bilan iishlash
# narhlar=[3200,1200,5200,4821,12345]
# print(f"sizning javobingiz quydagicha {narhlar[0]+narhlar[-1]}")  
# yigindi=f'{narhlar[1]+narhlar[-2]}'
# print("siz kiritgan  javobingiz quydagicha",yigindi)
narhlar=[1,2,3,4,5,6,7,8,9]
mevalar=['olma','banan','shaftoli', 'o\'rik','gilos']
mashinalar=['laseti','gentra','cobalt','malibu','nexia','damas']
bozorliklar=['un','yo\'','gosht','tuxum', 'kartoshka']
# append funksiyasini  ishlash jarayoni

# print(f'{mevalar.append('ananas')}',mevalar) bu xolda funksiyalar ishlamaydi

# ismlar=[]
# ismlar.append("sanjarbek")
# ismlar.append("Ilhomjon")
# ismlar.append("JAmshid")
# # print(ismlar)


# insert funksiyasi  ishlash jaryoni

# ismlar.insert(3,'Luhmonjon')
# print(ismlar)

# mashinalar.insert(-1-1,'matiz')
# mashinalar=[m.upper() for m in mashinalar]
# print(mashinalar)

# mashinalar=[m.upper() for m in mashinalar if m=='matiz']
# print(mashinalar)

# narhlar.insert(0,1200+4)
# for n in narhlar:
#     if n==1204:
#         print(n)

# del funksiyasi ishlash jarayoni

# del bozorliklar[0]
# print(bozorliklar)
# print(f'{ del bozorliklar[0]}')  del — f-string ichida ishlamaydi ❌

# maxsulotlar=[]
# del bozorliklar[0]
# for i in bozorliklar:
#     maxsulotlar.append(i)
# print(maxsulotlar)


# count funkisayis ishlash taribi  quydagicha  => ruyhatdagi elmentlar sonini  chiqaradi

# print(mevalar.count("olma"))
# tabiiy=f'{mevalar.copy()}'
# print(tabiiy)
# tabiiy=mevalar.copy()
# print(tabiiy)



#extend  funksiyasi  ishlash tartibi  =>  ikki ruyhatini  bir biriga qushib beradi.

# mevalar.extend(bozorliklar)
# print(mevalar)
# f"{mevalar.extend(bozorliklar)}"
# for i in mevalar:
#     if i == 'kartoshka':
#         print(i)



 # reverse funksiyasi ishlash tartibi  bunda ruyhatni teskari taribda  qilib beradi.

# mevalar.reverse()
# mevalar=[i.upper() for i in mevalar  if i=='banan']
# print(mevalar)


# print(list(range(0,10)))


# print(len(mevalar[0]))
# x=f'{len(mevalar[1])}'
# print(x)

#  mevalar ruyhatdagi  barcha elemantlarni barchasini  uzunligini chiqarib beradi

# for meva in mevalar:
#     print(len(meva))


# mevalar ruyhatdagi  elemantning  uzunligi  5 ga teng bulganlarni  chiqarib beradi

# for meva in mevalar:
#     if len(meva)==5:
#         print(meva)