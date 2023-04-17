from django.urls import path

from cv.views.cv import CVCreateView, CVDetailView, JobExpCreateView

urlpatterns = [
    path('cv/create/about_me/', CVCreateView.as_view(), name='cv_create'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('cv/<int:pk>/create/about_job/', JobExpCreateView.as_view(), name='job_create'),
]
