from django.contrib import admin
from .models import Coaching,Team,Profile,OutboundMonitoringForm

admin.site.register(Coaching)
admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(OutboundMonitoringForm)