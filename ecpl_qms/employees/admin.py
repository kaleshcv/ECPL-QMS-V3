from django.contrib import admin
from .models import Team,Profile,OutboundMonitoringForm,InboundMonitoringForm,EmailMonitoringForm,ChatMonitorinForm

admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(OutboundMonitoringForm)
admin.site.register(InboundMonitoringForm)
admin.site.register(EmailMonitoringForm)
admin.site.register(ChatMonitorinForm)

