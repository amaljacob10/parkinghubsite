from django.contrib import admin
from .models import service_station,Booking,rasperry,ProcessedImage,Subscription,UserSubscription,EventBooking
# Register your models here.
admin.site.register(service_station)
admin.site.register(Booking)
admin.site.register(rasperry)
admin.site.register(ProcessedImage)
admin.site.register(Subscription)
admin.site.register(EventBooking)

from django.contrib import admin
from .models import UserFeedback

@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback_text', 'created_at')
    search_fields = ('user__username', 'feedback_text')
    list_filter = ('created_at', 'user')
