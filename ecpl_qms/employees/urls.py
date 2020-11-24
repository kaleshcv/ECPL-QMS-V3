
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    path('agenthome',agenthome),
    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('qahome',qahome),
    path('coaching/<int:pk>',empCoachingView),
    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('outbound-coaching-form',outboundCoachingform),
    path('inbound-coaching-form',inboundCoachingform),
    path('email-coaching-form',emailmonitoringform),
    path('chat-coaching-form',chatmonitoringform),


]
