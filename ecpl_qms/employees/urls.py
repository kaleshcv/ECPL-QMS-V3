
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

    path('Monitoring-Form-new-series-common',newSeriesMonForms),

    path('domestic-email-chat-mon-form',domesticChatEmail),
    path('clear-view',clearView),
    path('printerpix-monform',printerPix),

    path('upfront-online-llc',upfrontOnlineMonForm),
    path('micro-distributing',microDistributingMonForm),
    path('jj-studio',jjStudioMonform),
    path('pluto-management',plutoManagement),
    path('sterling-strategies',sterlingStrategies),


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
    path('coaching-view-qa-all/<str:process>/<int:pk>',coachingViewQaDetailed),


    path('qa-open-status-coachings-view/<int:pk>',qacoachingViewOpenAll),

    path('campaign-wise-coaching-view',campaignwiseCoachings),
    path('campaign-wise-coaching-view-qa',campaignwiseCoachingsQA),

    path('campaign-wise-coaching-view-agent',campaignwiseCoachingsAgent),

    path('employee-wise-report', employeeWiseReport),
    path('manager-wise-report', managerWiseReport),


    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('campaign-view',campaignView),
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
    path('campaign-detailed-view/<str:cname>',campaignwiseDetailedReport),

    path('fame-house-full-report',fameHouseFullReport),

    path('export-data',exportAuditReport),
    path('export-data-qa',exportAuditReportQA),

    path('adduser',addtoUserModel),
    path('update-email-address/<int:pk>',updateEmailAddress),

    path('update-profile',updateProfile),
    path('checkprofile',checkProfile),

    #path('add-single-profile',addSingleProfile),

    path('powerbi-test',powerBITest),

    path('process-change',processNameChanger),

    path('desi-changer',desiChanger),
]
