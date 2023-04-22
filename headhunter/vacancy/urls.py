from django.urls import path
from vacancy.views.vacancy import (VacancyCreateView,VacancyDetailView,
                                   VacancyUpdateView, VacancyListView, UpdateListView,
                                   CompanyVacanciesView, IsPublishView, VacancyDeleteView
                                   )
from vacancy.views.application import ApplyVacancyView, UserApplicationsView, ApplicantsView
from vacancy.views.chat import ChatView, ChatListView

urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>/detail/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>/delete', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('apply_vacancy/<int:vacancy_id>/', ApplyVacancyView.as_view(), name='apply_vacancy'),
    path('vacancy/<int:pk>/publishing/', IsPublishView.as_view(), name='vacancy_publish'),
    path('vacancy/<int:pk>/update_list', UpdateListView.as_view(), name='update_list'),
    path('my_applications/', UserApplicationsView.as_view(), name='my_applications'),
    path('vacancies_company/<int:pk>/', CompanyVacanciesView.as_view(), name='company_vacancies'),
    path('applicants/', ApplicantsView.as_view(), name='applicants'),
    path('chat/<int:vacancy_id>/<int:applicant_id>/', ChatView.as_view(), name='chat'),
    path('chats/', ChatListView.as_view(), name='chats'),
]