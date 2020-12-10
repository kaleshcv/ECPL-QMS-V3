
from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    #Guidelines
    path('outbound-monitoring-guidelines',outboundGuidelines),
    path('inbound-monitoring-guidelines',inboundGuidelines),
    path('chat-monitoring-guidelines',chatGuidelines),
    path('email-monitoring-guidelines',emailGuidelines),

    # Monitoring Forms
    path('ECPL-EVA&NOVO-Monitoring-Form-chat',chatCoachingformEva),
    path('ECPL-Pod-Father-Monitoring-Form-chat',chatCoachingformPodFather),
    path('ECPL-INBOUND-CALL-MONITORING-FORM',inboundCoachingForm),


    path('agenthome',agenthome),
    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('qahome',qahome),

    # Coaching Views
    path('coaching-view-eva-chat/<int:pk>',empCoachingViewEvachat),
    path('coaching-view-eva-chat-qa/<int:pk>',qaCoachingViewEvachat),
    path('coaching-view-pod-chat/<int:pk>',empCoachingViewPodchat),
    path('coaching-view-pod-chat-qa/<int:pk>',qaCoachingViewPodchat),


    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('campaign-view/<int:pk>',campaignView),
    path('add-coaching',selectCoachingForm),
    path('coaching-summary-view',coachingSummaryView),
    path('coaching-success',coachingSuccess),
    path('coaching-dispute',coachingDispute),

]
