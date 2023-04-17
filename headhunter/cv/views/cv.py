from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cv.models.cv import CV

from cv.forms import CVForm


class CVCreateView(CreateView):
    template_name = 'cv/cv_create.html'
    model = CV
    form_class = CVForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.pk})


class CVDetailView(DetailView):
    template_name = 'cv/cv_detail.html'
    model = CV
    context_object_name = 'cv'
