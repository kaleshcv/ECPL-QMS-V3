
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
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
    path('wit-digital',witDigitel),
    path('Printer-Pix-Master-Monitoring-Form-Chats-Email',printerPixChatsEmails),
    path('Printer-Pix-Master-Monitoring-Form-Inbound-Calls',printerPixInboundCalls),
    path('Monitoring-Form-Leads-Aadhya-Solution',leadsandSalesAadya),

    path('Monitoring-Form-Leads-Insalvage',leadsandSalesInsalvage),
    path('Monitoring-Form-Leads-Medicare',leadsandSalesMedicare),
    path('Monitoring-Form-Leads-CTS',leadsandSalesCTS),
    path('Monitoring-Form-Leads-Tentamus-Food',leadsandSalesTenamusFood),
    path('Monitoring-Form-Leads-Tentamus-Pet',leadsandSalesTenamusPet),
    path('Monitoring-Form-Leads-City-Security',leadsandSalesCitySecurity),
    path('Monitoring-Form-Leads-Allen-Consulting',leadsandSalesAllenConsulting),
    path('Monitoring-Form-Leads-system4',leadsandSalesSystem4),
    path('Monitoring-Form-Leads-Louisville',leadsandSalesLouisville),
    path('Monitoring-Form-Leads-Info-Think-LLC',leadsandSalesInfoThink),
    path('Monitoring-Form-Leads-PSECU',leadsandSalesPSECU),
    path('Monitoring-Form-Leads-Get-A-Rates',leadsandSalesGetRates),
    path('Monitoring-Form-Leads-Advance-Consultant',leadsandSalesAdvance),


#### Credentials

    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('change_password',change_password),

    path('agenthome',agenthome),
    path('qahome',qahome),
    path('manager-home',qualityDashboardMgt),
    path('quality-dashboard-mgt',qualityDashboardMgt),


    path('quality-dashboard',qualityDashboard),


    # Coaching Views
    path('coaching-view-emp/<str:process>/<int:pk>',coachingViewAgents),


    path('coaching-view-eva-chat-qa/<int:pk>',qaCoachingViewEvachat),
    path('coaching-view-pod-chat/<int:pk>',empCoachingViewPodchat),
    path('coaching-view-pod-chat-qa/<int:pk>',qaCoachingViewPodchat),

    path('coaching-view-inbound-qa/<int:pk>',qaCoachingviewNucleus),

    path('coaching-view-fame-house-qa/<int:pk>',qaCoachingviewFamehouse),

    path('coaching-view-fla-qa/<int:pk>',qaCoachingviewFLA),

    path('coaching-view-mt-qa/<int:pk>',qaCoachingviewMt),

    path('coaching-view-mov-ins-qa/<int:pk>',qaCoachingviewMovIns),

    path('coaching-view-wit-qa/<int:pk>',qaCoachingviewWit),

    path('coaching-view-tonn-chat-qa/<int:pk>',qaCoachingviewTonnchat),

    path('coaching-view-pix-chat-qa/<int:pk>',qaCoachingviewPixchat),

    path('coaching-view-pix-inbound-qa/<int:pk>',qaCoachingviewPixinbound),

    path('coaching-view-aadya-qa/<int:pk>',qaCoachingviewAadya),
    path('coaching-view-insalvage-qa/<int:pk>',qaCoachingviewInsalvage),
    path('coaching-view-medicare-qa/<int:pk>',qaCoachingviewMedicare),
    path('coaching-view-cts-qa/<int:pk>',qaCoachingviewCts),
    path('coaching-view-tfood-qa/<int:pk>',qaCoachingviewTfood),
    path('coaching-view-tpet-qa/<int:pk>',qaCoachingviewTpet),
    path('coaching-view-city-qa/<int:pk>',qaCoachingviewCity),
    path('coaching-view-allen-qa/<int:pk>',qaCoachingviewAllen),
    path('coaching-view-system4-qa/<int:pk>',qaCoachingviewSystem4),
    path('coaching-view-louis-qa/<int:pk>',qaCoachingviewLouis),
    path('coaching-view-info-qa/<int:pk>',qaCoachingviewInfo),
    path('coaching-view-psecu-qa/<int:pk>',qaCoachingviewPsecu),
    path('coaching-view-get-qa/<int:pk>',qaCoachingviewGet),
    path('coaching-view-advance-qa/<int:pk>',qaCoachingviewAdvance),


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
    path('coaching-dispute/<int:pk>',coachingDispute),

    # Summary
    # categorywise
    path('inbound-summary',inboundSummary),
    path('chat-summary',chatSummary),
    path('leads-summary',leadsSummary),
    path('outbound-summary',leadsSummary),  # Same as Leads
    path('other-summary',otherSummary),
    path('email-summary',emailSummary),

    ##############3
    path('campaign-detailed-view',campaignwiseDetailedReport),

    path('fame-house-full-report',fameHouseFullReport),

    path('export-data/<str:campaign>',exportFameHouse)

]
