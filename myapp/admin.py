from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, FullAddress, Enquiry, Plan, Record, OTP
from django.utils.html import format_html
from .models import JobApplication

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'phone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'phone', 'is_active', 'is_staff')

class UserAdmin(DefaultUserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # Define the fields to display in the list view
    list_display = ('email', 'firstname', 'lastname', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'firstname', 'lastname', 'phone')
    ordering = ('email',)

    # Define the fields and their order in the detail view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define the fields and their order in the add view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'phone', 'password1', 'password2')}
        ),
    )
    
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, UserAdmin)
admin.site.register(FullAddress)
admin.site.register(Enquiry)
admin.site.register(Plan)
admin.site.register(Record)
admin.site.register(OTP)

from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'highest_qualification', 'experience', 'company', 'cv')
    list_filter = ('highest_qualification', 'experience')
    search_fields = ('firstname', 'lastname', 'email')

    # Optionally, you can add functionality to view the CV directly
    def cv_link(self, obj):
        if obj.cv:
            return format_html('<a href="{}">View CV</a>', obj.cv.url)
        return "No CV"
    
    cv_link.short_description = 'CV'

    # Add cv_link to the list_display
    list_display += ('cv_link',)

from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'job_type', 'location', 'posted_at')
    search_fields = ('title', 'company_name')
