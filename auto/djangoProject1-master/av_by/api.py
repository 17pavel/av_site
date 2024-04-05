
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .serializers import *

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-data_create')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def NewCar(self, request, newCar):
        if request.method == 'POST':
            city = City.objects.get(name=request.data.get(newCar.city_car))

            Car.objects.get_or_create(
                mark_car=request.data.get(newCar.mark_car),
                model_car=request.data.get(newCar.model_car),
                generation=request.data.get(newCar.generation),
                year=int(request.data.get(newCar.year)),
                body=request.data.get(newCar.body),
                motor=request.data.get(newCar.motor),
                price=int(request.data.get(newCar.price)),
                transmission=request.data.get(newCar.transmission),
                drive=request.data.get(newCar.drive),
                volume=request.data.get(newCar.volume),
                photo=request.data.get(newCar.photo),
                vin=request.data.get(newCar.vin),
                mileage=request.data.get(newCar.mileage),
                color=request.data.get(newCar.color),
                condition=request.data.get(newCar.condition),
                description=request.data.get(newCar.description),
                exchange=request.data.get(newCar.exchange),
                city_id=request.data.get(newCar.city_car),
                user=request.data.get(newCar.user),
            )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    def NewUser(self, request, newUser):
        if request.method == 'POST':
            user_phone = request.data.get(newUser.phone)
            user_name = request.data.get(newUser.name)
            user_password = request.data.get(newUser.password)
            us = User.objects.get_or_create(name=user_name, phone=user_phone, password=user_password)
        return Response(us, status=status.HTTP_200_OK)

