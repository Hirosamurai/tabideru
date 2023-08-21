from django.urls import path

from . import views


app_name = 'tabi'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('hotel/', views.HotelView.as_view(), name="hotel"),
    path('airticket/', views.AirticketView.as_view(), name="airticket"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('restaurant/', views.RestaurantView.as_view(), name="restaurant"),
    path('restaurant/<str:restaurantid>', views.Restaurantidview.as_view(), name="restaurantid"),
    path('mylist/', views.MylistView.as_view(), name="mylist"),
]
