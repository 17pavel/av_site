from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view

from django.shortcuts import render

from av_by.api import UserViewSet
from av_by.models import City, Car, User
from av_by.parsing import mark_car, vin_car, car_des, condition_car, color_car, mileage_car, photo_car, volum_car, \
    price_car, year_car, drive_car, motor_car, body_car, generation_car, model_car, car_city, user_phone, user_car, \
    gearbox_car

from av_by.serializers import CarSerializer, UserSerializer


class CarAPI(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


for k, v in user_car.items():
    us = User()
    try:
        us.id = k
        us.name = v
        us.phone = user_phone[k]
        us.save()
    except:
        pass


for key,val in mark_car.items():

    car = Car()

    ci = City
    try:
        cit = ci.objects.get(name=car_city[key])
    except:
        cit = ci.objects.get(name='Минск')
    car.id = key
    car.user_id = key
    try:
        car.transmission = gearbox_car[key]
    except KeyError:
        pass
    try:
        car.mark_car = val
        car.model_car = model_car[key]
        car.generation = generation_car[key]
        car.body = body_car[key]
        car.motor = motor_car[key]
        car.drive = drive_car[key]
        car.year = int(year_car[key])
        car.price = price_car[key]
        car.volume = volum_car[key]
        car.photo = photo_car[key]
        car.mileage = mileage_car[key]
        car.color = color_car[key]
        car.condition = condition_car[key]
        car.description = car_des[key]
        try:
            car.vin = vin_car[key]
        except:
            pass

        car.city_id_id = cit.id
        car.save()
    except:
        pass

@api_view(['GET', 'POST'])
def AddUser(request):
    if request.method == 'POST':
        name = request.data.get('name')
        print(name)
    return Response(name)