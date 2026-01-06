from django.contrib import admin

# Register your models here.
from tracker.models import *

admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory)

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"
