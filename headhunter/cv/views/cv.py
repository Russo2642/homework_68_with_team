from cv.forms import CVForm
from cv.forms import JobExpForm
from cv.models.cv import CV
from cv.models import JobExperience
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView


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

