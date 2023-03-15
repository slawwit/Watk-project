from django.urls import path, include
from .views import licz_list, handle_licz, dostawy_list, dostawy_details, edit_dostawy, LicznikBazowyOkulickiegoViewSet
from rest_framework import routers
from .api import UserAuthentication


router = routers.DefaultRouter()
router.register(r'liczniki', LicznikBazowyOkulickiegoViewSet)


app_name = "okulickiego"
urlpatterns = [
    path('liczniki/', licz_list, name="liczniki"),
    path('dost/', dostawy_list, name="dost_okuli"),
    path('api/', include(router.urls)),
    path('api/auth/', UserAuthentication.as_view(), name="UserAuth"),
    path('liczniki/add/', handle_licz, name="add_liczniki"),
    path('dost/<int:stany_id>/', dostawy_details, name="details_dost"),
    path('dost/<int:stany_id>/edit/', edit_dostawy, name="edit_dost"),
]