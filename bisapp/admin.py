from django.contrib import admin
from bisapp .models import CustomUser
from bisapp .models import UserProfile
from bisapp .models import DocumentRequest
from bisapp .models import IncidentReport
from bisapp .models import Contact





admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(DocumentRequest)
admin.site.register(IncidentReport)
admin.site.register(Contact)
