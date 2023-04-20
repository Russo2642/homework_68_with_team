from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from vacancy.forms import VacancyForm
from vacancy.models import Vacancy


class VacancyListView(ListView):
    template_name = 'vacancies.html'
    model = Vacancy
    context_object_name = 'vacancies'


class VacancyCreateView(CreateView):
    template_name = 'vacancy_create.html'
    form_class = VacancyForm
    model = Vacancy

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('vacancy_detail', pk=form.instance.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.author.pk})


class VacancyDetailView(DetailView):
    template_name = 'vacancy_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'

    def get_object(self, queryset=None):
        try:
            return Vacancy.objects.get(pk=self.kwargs['pk'])
        except Vacancy.DoesNotExist:
            return redirect('index')


class VacancyUpdateView(UpdateView):
    template_name = 'vacancy_update.html'
    form_class = VacancyForm
    model = Vacancy
    context_object_name = 'vacancy'

    def get_success_url(self):
        return reverse('vacancy_detail', kwargs={'pk': self.object.pk})
