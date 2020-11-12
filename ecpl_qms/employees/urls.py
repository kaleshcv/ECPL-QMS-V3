
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    path('agenthome',agenthome),
    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('addcoaching',addcoaching),
    path('qahome',qahome),
    path('coaching/<int:pk>',empCoachingView),
    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('outbound-coaching-form',outboundCoachingform),


]
