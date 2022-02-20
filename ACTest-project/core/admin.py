from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


from core import models

class UserAdmin(BaseUserAdmin):
	ordering = ['id']
	list_display = ['email', 'name']
	fieldsets = (
		# title and fields definition
		(None, {'fields': ('email', 'password')}),
		(_('Personal Info'), {'fields': ('name', )}),
		(
			_('Permissions'), 
			{'fields': ('is_active', 'is_staff', 'is_superuser')}
		),
		(_('Important dates'), {'fields': ('last_login', )}), # last seen day can be added here
	)

	add_fieldsets = (
		(None, {
			# defaults from the user admin documentation
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		}), # with a comma, because we just have one item
	)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)