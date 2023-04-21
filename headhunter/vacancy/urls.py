from django.urls import path
from vacancy.views.vacancy import VacancyCreateView, VacancyDetailView, VacancyUpdateView, VacancyListView, CompanyVacanciesView
from vacancy.views.application import ApplyVacancyView, UserApplicationsView


urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>/detail/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('apply_vacancy/<int:vacancy_id>/', ApplyVacancyView.as_view(), name='apply_vacancy'),
    path('my_applications/', UserApplicationsView.as_view(), name='my_applications'),
    path('vacancies_company/<int:pk>/', CompanyVacanciesView.as_view(), name='company_vacancies'),
]