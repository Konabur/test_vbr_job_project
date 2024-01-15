from django.utils.html import format_html
from django.contrib import admin
from .models import User, Event, Organization


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'get_organizations')
    search_fields = ('email', 'phone_number')

    def get_organizations(self, obj):
        return ', '.join(o.title for o in obj.organizations.all())

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'preview_image')

    def preview_image(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url)) if obj.image else "No Image"
    
    preview_image.short_description = 'Image Preview'


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'postcode')
    search_fields = ('title', 'address', 'postcode')
