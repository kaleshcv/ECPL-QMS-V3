from django.contrib import admin

from .models import *

admin.site.register(Team)
admin.site.register(Profile)

# Monitoring Forms

admin.site.register(ChatMonitoringFormEva)     # view done
admin.site.register(ChatMonitoringFormPodFather)     # view done
admin.site.register(InboundMonitoringFormNucleusMedia)     # view done
admin.site.register(FameHouseMonitoringForm)    # view done
admin.site.register(FLAMonitoringForm)     # view done
admin.site.register(MasterMonitoringFormGetaRatesPSECU)
admin.site.register(MasterMonitoringFormMovementInsurance)
admin.site.register(MasterMonitoringFormMTCosmetics)      # view done
admin.site.register(MasterMonitoringFormTonnChatsEmail)     # view done
admin.site.register(MasterMonitoringFormTonnCoaInboundCalls)
admin.site.register(MonitoringFormLeadsAadhyaSolution)
admin.site.register(PrinterPixMasterMonitoringFormInboundCalls)
admin.site.register(PrinterPixMasterMonitoringFormChatsEmail)
admin.site.register(WitDigitalMasteringMonitoringForm)



