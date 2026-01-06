from django.contrib import admin

# Register your models here.
from tracker.models import *

admin.site.register(CurrentBalance)

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "description",
        "amount",
        "expense_type",
    ]

admin.site.register(TrackingHistory, TrackingHistoryAdmin)

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"
