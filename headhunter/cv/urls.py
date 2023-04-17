from django.urls import path

from cv.views.cv import CVCreateView, CVDetailView

urlpatterns = [
    path('cv/create/', CVCreateView.as_view(), name='cv_create'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
]
