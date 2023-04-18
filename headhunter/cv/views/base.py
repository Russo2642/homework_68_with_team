from cv.models import CV
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.db.models import Q, Max
from django.shortcuts import render
from django.views import View


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        cv = CV.objects.all()
        context = {
            'cvs': cv,
        }
        return render(request, 'index.html', context=context)
