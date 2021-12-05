from django.contrib import admin
from .models import Users,Links,Visits

# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('verified','email','created_at','updated_at','_opcoes')
    search_fields = ("email",)
    readonly_fields = ('created_at','updated_at' )
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

    def get_model_perms(self, request, *args, **kwargs):
        """
                Return a dict of all perms for this model. This dict has the keys
                ``add``, ``change``, ``delete``, and ``view`` mapping to the True/False
                for each of those actions.
                """
        return {
            'add': False,
            'change': self.has_change_permission(request),
            'delete': self.has_delete_permission(request),
        }
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
            'fields': ['target',
                       'address', 
                       'description',
                       'visit_count',
                       'user',
                       'password',
                       'banned',
                       'expire_in',
                       'created_at',
                       'updated_at']
        }),
    ]

    # def get_model_perms(self, *args, **kwargs):
    #     """
    #             Return a dict of all perms for this model. This dict has the keys
    #             ``add``, ``change``, ``delete``, and ``view`` mapping to the True/False
    #             for each of those actions.
    #             """
    #     return {}
