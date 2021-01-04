
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
    path('ECPL-Fame-House-MONITORING-FORM',fameHouse),
    path('ECPL-FLA-MONITORING_FORM',flaMonForm),
    path('ECPL-Lead-sales-MONITORING_FORM',leadsandSalesMonForm),
    path('ECPL-Email-chat-MONITORING_FORM',emailAndChatmonForm),
    path('Master-Monitoring-Form-Movement-Insurance',movementInsurance),
    path('Printer-Pix-Master-Monitoring-Form-Chats-Email',printerPixChatsEmails),
    path('Printer-Pix-Master-Monitoring-Form-Inbound-Calls',printerPixInboundCalls),



    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),

    path('agenthome',agenthome),
    path('qahome',qahome),
    path('manager-home',qualityDashboardMgt),
    path('quality-dashboard-mgt',qualityDashboardMgt),


    path('quality-dashboard',qualityDashboard),

    path('employee-wise-report',employeeWiseReport),
    path('manager-wise-report',managerWiseReport),



    # Coaching Views
    path('coaching-view-eva-chat/<int:pk>',empCoachingViewEvachat),
    path('coaching-view-eva-chat-qa/<int:pk>',qaCoachingViewEvachat),
    path('coaching-view-pod-chat/<int:pk>',empCoachingViewPodchat),
    path('coaching-view-pod-chat-qa/<int:pk>',qaCoachingViewPodchat),


    path('qa-open-status-coachings-view/<int:pk>',qacoachingViewOpenAll),

    path('campaign-wise-coaching-view',campaignwiseCoachings),
    path('campaign-wise-coaching-view-agent',campaignwiseCoachingsAgent),


    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('campaign-view/<int:pk>',campaignView),
    path('add-coaching',selectCoachingForm),
    path('coaching-summary-view',coachingSummaryView),
    path('coaching-success',coachingSuccess),
    path('coaching-dispute',coachingDispute),

    # Summary



]
