from cv.forms import CVForm
from cv.forms import JobExpForm
from cv.models.cv import CV
from cv.models import JobExperience
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from vacancy.models import Application


class CVCreateView(CreateView):
    template_name = 'cv/cv_create.html'
    model = CV
    form_class = CVForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job_create', kwargs={'pk': self.object.pk})


class CVDetailView(DetailView):
    template_name = 'cv/cv_detail.html'
    model = CV
    context_object_name = 'cv'


class CVUpdateView(UpdateView):
    template_name = 'cv/cv_update.html'
    model = CV
    form_class = CVForm

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.pk})


class CVDeleteView(UserPassesTestMixin, DeleteView):
    model = CV

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user_id})

    def test_func(self):
        return self.get_object().user == self.request.user


class JobExpCreateView(CreateView):
    template_name = 'cv/job_create.html'
    model = JobExperience
    form_class = JobExpForm

    def form_valid(self, form):
        cv = get_object_or_404(CV, pk=self.kwargs.get('pk'))
        job_exp = form.save(commit=False)
        job_exp.cv = cv
        job_exp.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class JobExpUpdateView(UpdateView):
    template_name = 'cv/job_update.html'
    model = JobExperience
    form_class = JobExpForm
    context_object_name = 'job_exp'

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.cv_id})


class UpdateButtonView(View):
    def post(self, request, pk):
        cv = get_object_or_404(CV, pk=pk)
        cv.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class IsPublishedView(View):
    def post(self, request, pk):
        cv = get_object_or_404(CV, pk=pk)
        if cv.is_published:
            cv.is_published = False
        else:
            cv.is_published = True
        cv.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CVListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_employer:
            applications = Application.objects.filter(vacancy__author=request.user)
            applicant_ids = [app.applicant.id for app in applications]
            cvs = CV.objects.filter(user__id__in=applicant_ids)
        else:
            cvs = CV.objects.filter(user=request.user)

        context = {
            'cvs': cvs,
        }
        return render(request, 'cv/cv_list.html', context=context)


