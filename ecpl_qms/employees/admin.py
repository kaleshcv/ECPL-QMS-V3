from django.contrib import admin
from .models import Team,Profile,OutboundMonitoringForm,InboundMonitoringForm

admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(OutboundMonitoringForm)
admin.site.register(InboundMonitoringForm)
