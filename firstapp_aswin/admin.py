from django.contrib import admin

from firstapp_aswin.models import Sign_in,Sign_up,HealthRecord,FinancialDetails,EducationalDetails

# Register your models here.

admin.site.register(Sign_in)
admin.site.register(Sign_up)
admin.site.register(HealthRecord)
admin.site.register(FinancialDetails)
admin.site.register(EducationalDetails)
