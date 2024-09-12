from django.contrib import admin
from .models import IntermediaryCloudAccess, CCEmail, CloudAccessEmail

class CCEmailInline(admin.TabularInline):
    model = CCEmail
    extra = 1  # Number of empty CC email fields to display by default

class CloudAccessEmailInline(admin.TabularInline):
    model = CloudAccessEmail
    extra = 1  # Number of empty cloud access email fields to display by default

@admin.register(IntermediaryCloudAccess)
class IntermediaryCloudAccessAdmin(admin.ModelAdmin):
    list_display = (
        'broker_agent_name', 
        'tin_no', 
        'vrn_registered', 
        'vrn_no', 
        'address', 
        'mobile_number', 
        'company_email'
    )
    search_fields = ('broker_agent_name', 'tin_no', 'vrn_no', 'company_email')
    list_filter = ('vrn_registered',)
    inlines = [CCEmailInline, CloudAccessEmailInline]

@admin.register(CCEmail)
class CCEmailAdmin(admin.ModelAdmin):
    list_display = ('intermediary_cloud_access', 'cc_email')
    search_fields = ('cc_email',)
    list_filter = ('intermediary_cloud_access',)

@admin.register(CloudAccessEmail)
class CloudAccessEmailAdmin(admin.ModelAdmin):
    list_display = ('intermediary_cloud_access', 'cloud_access_email')
    search_fields = ('cloud_access_email',)
    list_filter = ('intermediary_cloud_access',)
