from django.contrib import admin
from .models import (
    Article,
    Vacancy,

    )

admin.site.register(Article)
admin.site.register(Vacancy)