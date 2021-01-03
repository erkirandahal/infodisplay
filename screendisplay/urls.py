from django.urls import path
from . import views
from . views import (
    ArticleListView,
    PublicProcurementCreateView,
    PublicProcurementListView,
    PublicProcurementDetailView,
    PublicProcurementUpdateView,
    PublicProcurementDeleteView,
    VacancyCreateView,
    VacancyListView,
    VacancyDetailView,
    VacancyUpdateView,
    VacancyDeleteView,
    OfficialCreateView,
    OfficialListView,
    OfficialDetailView

    )
urlpatterns = [
    path('', ArticleListView.as_view(), name='screendisplay-home'),
    path('publicprocurement/create/', PublicProcurementCreateView.as_view(), name='publicprocurement-create'),
    path('publicprocurement/list/', PublicProcurementListView.as_view(), name='publicprocurement-list'),
    path('publicprocurement/<int:pk>/', PublicProcurementDetailView.as_view(), name='publicprocurement-detail'),
    path('publicproocurement/update/<int:pk>', PublicProcurementUpdateView.as_view(), name='publicprocurement-update'),
    path('publicproocurement/delete/<int:pk>', PublicProcurementDeleteView.as_view(), name='publicprocurement-delete'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy-create'),
    path('vacancy/list/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancy/update/<int:pk>', VacancyUpdateView.as_view(), name='vacancy-update'),
    path('vacancy/delete/<int:pk>', VacancyDeleteView.as_view(), name='vacancy-delete'),
    path('official/create/', OfficialCreateView.as_view(), name='official-create'),
    path('official/list/', OfficialListView.as_view(), name='official-list'),
    path('official/<int:pk>/', OfficialDetailView.as_view(), name='official-detail'),

]