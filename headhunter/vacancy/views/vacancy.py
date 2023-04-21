from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
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


class VacancyDeleteView(UserPassesTestMixin, DeleteView):
    model = Vacancy

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.author_id})

    def test_func(self):
        return self.get_object().author == self.request.user


class IsPublishView(View):
    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        if vacancy.is_published:
            vacancy.is_published = False
        else:
            vacancy.is_published = True
        vacancy.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class UpdateListView(View):
    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        vacancy.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

class CompanyVacanciesView(LoginRequiredMixin, ListView):
    template_name = 'vacancies_company.html'
    model = Vacancy
    context_object_name = 'vacancies'

    def get_queryset(self):
        company_id = self.kwargs['pk']
        return Vacancy.objects.filter(author_id=company_id)
