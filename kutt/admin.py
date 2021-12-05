from django.contrib import admin
from .models import Users,Links,Visits

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('verified','email','created_at','updated_at','_opcoes')
    search_fields = ("email",)
    readonly_fields = ('created_at','updated_at','_urlLinks' )
    # save_on_top = True
    # save_as = True
    fieldsets = [
        ('Geral', {
            'fields': ['email', 
                       'verified',
                       'banned',
                       'banned_by',
                       'password',
                       'created_at',
                       'updated_at']
        }),
    ]

# Register your models here.
@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('id','address','target','visit_count','user','expire_in','_opcoes')
    search_fields = ("target","address","description")
    readonly_fields = ('created_at','updated_at','visit_count' )
    # list_filter = ('user',)
    # save_on_top = True
    # save_as = True
    fieldsets = [
        ('Geral', {
            'fields': ['address', 
                       'description',
                       'visit_count',
                       'user',
                       'banned',
                       'expire_in',
                       'created_at',
                       'updated_at']
        }),
    ]