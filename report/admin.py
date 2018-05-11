from django.contrib import admin
from .models import Entity, User, Category, Product, Document, DocumentLines
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from report.models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = "Працівники"
    

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Entity)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Document)
admin.site.register(DocumentLines)
