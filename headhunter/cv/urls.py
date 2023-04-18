from django.urls import path

from cv.views.cv import CVCreateView, CVDetailView, JobExpCreateView, CVUpdateView, JobExpUpdateView, UpdateButtonView

from cv.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cv/create/about_me/', CVCreateView.as_view(), name='cv_create'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('cv/<int:pk>/about_me/update', CVUpdateView.as_view(), name='cv_update'),
    path('cv/<int:pk>/create/about_job/', JobExpCreateView.as_view(), name='job_create'),
    path('cv/<int:pk>/about_job/update/', JobExpUpdateView.as_view(), name='job_update'),

    path('cv/<int:pk>/update_button', UpdateButtonView.as_view(), name='update_button')
]
