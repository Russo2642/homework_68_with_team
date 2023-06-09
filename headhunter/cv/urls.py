from django.urls import path

from cv.views.cv import (
    CVCreateView,
    CVDetailView,
    CVDeleteView,
    JobExpCreateView,
    CVUpdateView,
    JobExpUpdateView,
    UpdateButtonView,
    IsPublishedView,
    CVListView,
    get_to_pdf
)

from cv.views.base import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cv/', CVListView.as_view(), name='my_cv'),
    path('cv/create/about_me/', CVCreateView.as_view(), name='cv_create'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('cv/<int:pk>/about_me/update', CVUpdateView.as_view(), name='cv_update'),
    path('cv/<int:pk>/delete', CVDeleteView.as_view(), name='cv_delete'),
    path('cv/<int:pk>/create/about_job/', JobExpCreateView.as_view(), name='job_create'),
    path('cv/<int:pk>/about_job/update/', JobExpUpdateView.as_view(), name='job_update'),
    path('cv/<int:pk>/update_button', UpdateButtonView.as_view(), name='update_button'),
    path('cv/<int:pk>/publishing/', IsPublishedView.as_view(), name='publishing'),
    path('cv/<int:pk>/pdf/', get_to_pdf, name='pdf')
]
