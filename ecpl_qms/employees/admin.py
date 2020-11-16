from django.contrib import admin
from .models import Team,Profile,OutboundMonitoringForm

admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(OutboundMonitoringForm)