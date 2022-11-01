from django.contrib import admin

# Register your models here.
from Gold_Bk_app.models import *
from Gold_Bk_app.views import CustomAuthToken

admin.site.register(Usuario),
admin.site.register(Activo),
admin.site.register(Cuenta),
admin.site.register(Trade),


