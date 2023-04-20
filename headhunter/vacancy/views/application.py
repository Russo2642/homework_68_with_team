from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from vacancy.models import Application, Vacancy


class UserApplicationsView(LoginRequiredMixin, View):
    template_name = 'vacancy_list.html'

    def get(self, request):
        applications = Application.objects.filter(applicant=request.user)
        return render(request, self.template_name, {'applications': applications})


class ApplyVacancyView(LoginRequiredMixin, View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        cv = request.user.cv.first()

        if cv and not Application.objects.filter(applicant=request.user, vacancy=vacancy).exists():
            Application.objects.create(applicant=request.user, vacancy=vacancy)

        return redirect(reverse('my_applications'))
