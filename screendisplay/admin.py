from django.contrib import admin
from .models import (
    Article,
    Vacancy,
    PublicProcurement,
    Official,
    OfficeInfo
    )

admin.site.register(Article)
admin.site.register(Vacancy)
admin.site.register(PublicProcurement)
admin.site.register(Official)
admin.site.register(OfficeInfo)