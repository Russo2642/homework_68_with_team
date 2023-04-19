from django.urls import path
from vacancy.views.vacancy import VacancyCreateView, VacancyDetailView

urlpatterns = [
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>/detail/', VacancyDetailView.as_view(), name='vacancy_detail'),
]