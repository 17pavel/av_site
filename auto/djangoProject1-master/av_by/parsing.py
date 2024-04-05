import random


from bs4 import BeautifulSoup
import requests

r = requests.get('https://autobuy.by/')
bs = BeautifulSoup(r.text,'lxml')

all = bs.find_all('img')
for i in all:
    d = str(i).split('src="')
    if d[1].find('svg"')==-1:
        s = d[1][0:d[1].find('jpg"') + 3]
    else:
        s = d[1][0:d[1].find('svg"')+3]
    if len(s)>3:
        q = 'https://autobuy.by'+s

# https://autobuy.by/autobuy_logo.svg
# https://autobuy.by/images/all/cars/2024/01/02/photo_212x146_6ef5735dfaaac482f5b34c37aecf3c1e.webp

av = requests.get('https://autobuy.by/cars')
pars = BeautifulSoup(av.text, 'lxml')

car = pars.find_all('div')

mark = list()



for i in car:
    #print(i)
    if 'Марка' in i.text:
        mark.append(i.text)


mark_av2 = mark[0][13:mark[0].find('УАЗ')+3].split('\n')
#print(mark_av2)
mark_av = {}
for i in mark_av2:
    mark_av[i[0:3]] = i

#print(mark_av)
car_body = {'Se': 'Седан','Uni': 'Универсал','Hech_3': 'Хэтчбек 3 дв', 'Hech_5': 'Хэтчбек 5 дв', 'SUV_3': 'Внедорожник 3 дв', 'SUV_5': 'Внедорожник 5 дв', 'Kup': 'Купе',
            'Lift': 'Лифтбек', 'Pik' : 'Пикап', 'Kabri': 'Кабриолет', 'Van': 'Фургон', 'Mini': 'Минивэн','Rod': 'Родстер','Lim': 'Лимузин','Kross': 'Кроссовер'}
gearbox = {'Mech': 'Механика','Auto': 'Автомат','Rob': 'Робот','Var': 'Вариатор'}
motor = {'Benz': 'Бензиновый','Diz': 'Дизельный','Elektro': 'Электрический','Gibr': 'Гибрид'}
drive_unit = {'Forw': 'Передний','Back': 'Задний','All': 'Полный'}
#print(mark_av)
m = requests.get('https://autobuy.by/cars/acura')
mod = BeautifulSoup(m.text, 'lxml')
engine_capacity = list()
mo = mod.find_all('option')
for i in mo:
    if 'л' in i.text:
        engine_capacity.append(i.text)

volum = list()
for i in engine_capacity:
    if len(i)<6:
        volum.append(i)

div_car = pars.find_all('div', class_='car__item-front')
mark_car = {}
model_car = {}
generation_car = {}
gearbox_car = {}
price_car = {}
body_car = {}
motor_car = {}
year_car = {}
drive_car = {}
volum_car = {}
photo_car = {}
mileage_car = {}
color_car = {}
condition_car = {}
vin_car = {}
a_car = {}
user_car = {}
car_city = {}
car_des = {}
gener = list()
user_phone = {}
img_arr = list()
def phone():
    arr = list()
    phone_pre = random.choice(['29', '33', '44', '25'])
    for i in range(1,7):
        num = random.randint(0,9)
        arr.append(str(num))
        if arr[0] == '0':
            arr[0] = '1'
    number = ''.join(arr)
    phone = phone_pre+number
    return phone

for i in div_car:
    car_all = str(i).split('<a href="')
    ad = car_all[1][0:car_all[1].find('"')]
    ad_all = 'https://autobuy.by'+str(ad)
    adt = requests.get(ad_all)
    soup = BeautifulSoup(adt.text, 'lxml')
    div_des = soup.find_all('div', class_='car__msg')


    div_ad_right = soup.find('div', class_='car-info__right')
    div_contact = soup.find_all('div', class_='big__btn')
    for p in div_contact:
        numb_con = str(p).split('data-car="')
        for w in numb_con:
            if 'data-hystmodal-contact' in str(w):
                atr = str(w)[0:4]
    user_phone[atr] = phone() #Телефон
    for x in div_des:
        car_des[atr] = x.text
    for k in div_ad_right:
        param = str(k.text).split('\n')
        for t in param:
            if t == '':
                param.remove(t)
        if len(param)==7:
            price_car[atr]=int(param[0][0:-5].replace(' ',''))
        elif len(param)==29:
            volum_car[atr] = param[1][0:-1] #Объем двигателя
            motor_car[atr] = param[3]#Тип двигателя
            drive_car[atr] = param[5]# Привод
            gearbox_car[atr] = param[7]# Коробка передач
            body_car[atr] = param[9]# Кузов
            mileage_car[atr] = int(param[11].replace(' км', '').replace(',',''))# Пробег
            year_car[atr] = param[13][0:4]# Год
            condition_car[atr] = param[19]# Состояние
            color_car[atr] = param[25]# Цвет
        elif len(param)==12:
            user_car[atr] = param[0]# Владелец
            car_city[atr] = param[1].replace('г. ','')# город
    vin = soup.find_all('p', class_='params__value vin-title')
    for h in vin:
        if h.text!='':
            vin_car[atr] = h.text

    div_ad_left = soup.find('div', class_='wrap wrap_o car-info__left')

    for g in div_ad_left:
        marK_mod = str(g.text).split('\n')
        for u in marK_mod:
            if u == '':
                marK_mod.remove(u)
        if len(marK_mod)>2:
            mmg = marK_mod[0].split(' ')
            ma = mmg[0]
            mo = mmg[1]
            for h in range(2, len(mmg)):
                gener.append(mmg[h])
            ge = ' '.join(gener)
            gener.clear()
            mark_car[atr] = ma #Марка
            model_car[atr] =  mo #Модель
            generation_car[atr] = ge #Поколение
        img = str(g).split('src="')
        for d in img:
            #print(d)
            if 'https://autobuy.by/images/all/cars/' in d:
                if len(d[0:d.find('jpg')+3])>3:
                    img_arr.append(d[0:d.find('jpg')+3])
                elif len(d[0:d.find('png')+3])>3:
                    img_arr.append(d[0:d.find('png')+3])
        if len(img_arr)>=1:
            li = []
            for i in img_arr:
                if img_arr.index(i) < len(img_arr)/2:
                    li.append(i)

            photo_car[atr] = '~'.join(li)  # Фото




        img_arr.clear()



for i in range(84, 42, -1):
    volum.pop(i)

volum_drive = {}
for i in volum:
    volum_drive[i[0:3]]=i

