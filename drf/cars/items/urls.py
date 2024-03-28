from django.urls import path, include
# from rest_framework import routers

from . import views


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)
# router.register(r'item', ItemsViewSet)
# router.register(r'image', ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('category/', views.CategoryList.as_view()),
    path('item/', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemRetrive.as_view()),
    path('image/', views.ImageRetrive.as_view()),
    path('item/<int:pk>/update', views.ItemRetrieveUpdateDestroy.as_view()),

    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),

    path('users/', include('users.urls')),
]