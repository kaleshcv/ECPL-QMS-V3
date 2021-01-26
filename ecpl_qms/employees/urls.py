
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
    path('ECPL-Lead-sales-MONITORING_FORM-PSECU',leadsandSalesMonFormPsecu),
    path('ECPL-Email-chat-MONITORING_FORM',emailAndChatmonForm),
    path('Master-Monitoring-Form-Movement-Insurance',movementInsurance),
    path('wit-digital',witDigitel),
    path('Printer-Pix-Master-Monitoring-Form-Chats-Email',printerPixChatsEmails),
    path('Printer-Pix-Master-Monitoring-Form-Inbound-Calls',printerPixInboundCalls),
    path('Monitoring-Form-Leads-Aadhya-Solution',leadsandSalesAadya),



    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),

    path('agenthome',agenthome),
    path('qahome',qahome),
    path('manager-home',qualityDashboardMgt),
    path('quality-dashboard-mgt',qualityDashboardMgt),


    path('quality-dashboard',qualityDashboard),





    # Coaching Views
    path('coaching-view-eva-chat/<int:pk>',empCoachingViewEvachat),
    path('coaching-view-eva-chat-qa/<int:pk>',qaCoachingViewEvachat),
    path('coaching-view-pod-chat/<int:pk>',empCoachingViewPodchat),
    path('coaching-view-pod-chat-qa/<int:pk>',qaCoachingViewPodchat),
    path('coaching-view-inbound/<int:pk>',empCoachingviewNucleus),
    path('coaching-view-inbound-qa/<int:pk>',qaCoachingviewNucleus),
    path('coaching-view-fame-house/<int:pk>',empCoachingviewFamehouse),
    path('coaching-view-fame-house-qa/<int:pk>',qaCoachingviewFamehouse),
    path('coaching-view-fla/<int:pk>',empCoachingviewFLA),
    path('coaching-view-fla-qa/<int:pk>',qaCoachingviewFLA),
    path('coaching-view-mt/<int:pk>',empCoachingviewMt),
    path('coaching-view-mt-qa/<int:pk>',qaCoachingviewMt),
    path('coaching-view-mov-ins/<int:pk>',empCoachingviewMovIns),
    path('coaching-view-mov-ins-qa/<int:pk>',qaCoachingviewMovIns),
    path('coaching-view-wit/<int:pk>',empCoachingviewWit),
    path('coaching-view-wit-qa/<int:pk>',qaCoachingviewWit),
    path('coaching-view-tonn-chat/<int:pk>',empCoachingviewTonnchat),
    path('coaching-view-tonn-chat-qa/<int:pk>',qaCoachingviewTonnchat),
    path('coaching-view-pix-chat/<int:pk>',empCoachingviewPixchat),
    path('coaching-view-pix-chat-qa/<int:pk>',qaCoachingviewPixchat),
    path('coaching-view-pix-inbound/<int:pk>',empCoachingviewPixinbound),
    path('coaching-view-pix-inbound-qa/<int:pk>',qaCoachingviewPixinbound),
    path('coaching-view-aadya/<int:pk>',empCoachingviewAadya),
    path('coaching-view-aadya-qa/<int:pk>',qaCoachingviewAadya),


    path('qa-open-status-coachings-view/<int:pk>',qacoachingViewOpenAll),

    path('campaign-wise-coaching-view',campaignwiseCoachings),
    path('campaign-wise-coaching-view-agent',campaignwiseCoachingsAgent),

    path('employee-wise-report', employeeWiseReport),
    path('manager-wise-report', managerWiseReport),


    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('campaign-view/<int:pk>',campaignView),
    path('add-coaching',selectCoachingForm),
    path('coaching-summary-view',coachingSummaryView),
    path('coaching-success',coachingSuccess),
    path('coaching-dispute',coachingDispute),

    # Summary
    # categorywise
    path('inbound-summary',inboundSummary),
    path('chat-summary',chatSummary),
    path('leads-summary',leadsSummary),
    path('outbound-summary',leadsSummary),  # Same as Leads
    path('other-summary',otherSummary),
    path('email-summary',chatSummary),  # same as chat

]
