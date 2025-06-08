from django.contrib import admin

from employeApp.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = 'firstname', 'lastname', 'country'

admin.site.register(Member, MemberAdmin)
