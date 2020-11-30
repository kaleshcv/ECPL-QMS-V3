
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    path('agenthome',agenthome),
    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('qahome',qahome),
    path('coaching-view-outbound/<int:pk>',empCoachingViewOutbound),
    path('coaching-view-inbound/<int:pk>',empCoachingViewInbound),
    path('coaching-view-email/<int:pk>',empCoachingViewEmail),
    path('coaching-view-chat/<int:pk>',empCoachingViewChat),
    path('coaching-view-outbound-qa/<int:pk>',qaCoachingViewOutbound),
    path('coaching-view-inbound-qa/<int:pk>',qaCoachingViewInbound),
    path('coaching-view-email-qa/<int:pk>',qaCoachingViewEmail),
    path('coaching-view-chat-qa/<int:pk>',qaCoachingViewChat),
    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('outbound-coaching-form',outboundCoachingform),
    path('inbound-coaching-form',inboundCoachingform),
    path('email-coaching-form',emailmonitoringform),
    path('chat-coaching-form',chatmonitoringform),
    path('survey-coaching-form',surveyCoachingform),


]
