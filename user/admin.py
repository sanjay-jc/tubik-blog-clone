from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Custom_user
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.


class Customuseradmin(UserAdmin):
    add_form=CustomUserCreationForm
    form = CustomUserChangeForm
    model = Custom_user
    list_display=('email','is_staff','is_active')
    list_filter = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None,{"fields":("email","password")}),
        ("Permissions",{"fields":("is_staff","is_superuser","is_active","user_permissions","groups")})
    )

    add_fieldsets =(
        (None,{
            "classes":("wide",),
            "fields":(
                "email","password1","password2","is_staff",
                "is_active","groups","user_permissions"
            )
        }),
    )

    search_fields = ("email",)
admin.site.register(Custom_user,Customuseradmin)


