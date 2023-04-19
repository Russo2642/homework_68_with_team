from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from vacancy.forms import VacancyForm
from vacancy.models import Vacancy


class VacancyCreateView(CreateView):
    template_name = 'vacancy_create.html'
    form_class = VacancyForm
    model = Vacancy

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('vacancy_detail', pk=request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.author.pk})


class VacancyDetailView(DetailView):
    template_name = 'vacancy_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'