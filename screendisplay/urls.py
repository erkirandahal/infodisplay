from django.urls import path
from . import views
from . views import (
    ArticleListView,
    PublicProcurementCreateView,
    PublicProcurementListView,
    VacancyCreateView,
    VacancyListView,
    VacancyDetailView,

    )
urlpatterns = [
    path('', ArticleListView.as_view(), name='screendisplay-home'),
    path('publicprocurement/create/', PublicProcurementCreateView.as_view(), name='publicprocurement-create'),
    path('publicprocurement/list/', PublicProcurementListView.as_view(), name='publicprocurement-list'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy-create'),
    path('vacancy/list/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
]