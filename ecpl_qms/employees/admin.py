from django.contrib import admin

from .models import *

admin.site.register(Team)
admin.site.register(Profile)

# Monitoring Forms

admin.site.register(ChatMonitoringFormEva)
admin.site.register(ChatMonitoringFormPodFather)
admin.site.register(InboundMonitoringForm)
admin.site.register(FameHouseMonitoringForm)
admin.site.register(FLAMonitoringForm)
admin.site.register(LeadsandSalesMonForm)
admin.site.register(ChatandEmailMonForm)



