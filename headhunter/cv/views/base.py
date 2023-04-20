from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy
from cv.models.cv import CategoryChoice


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        category = request.GET.get('category')
        if category:
            vacancies = vacancies.filter(profession=category)

        sort = request.GET.get('sort')
        if sort == 'salary_asc':
            vacancies = vacancies.order_by('salary')
        elif sort == 'salary_desc':
            vacancies = vacancies.order_by('-salary')
        else:
            vacancies = vacancies.order_by('-updated_at')

        search = request.GET.get('search')
        if search:
            vacancies = vacancies.filter(Q(title__icontains=search) | Q(description__icontains=search))

        context = {
            'vacancies': vacancies,
            'CategoryChoice': CategoryChoice.choices,
            'selected_category': category,
            'selected_sort': sort,
            'search_query': search,
        }
        return render(request, 'index.html', context=context)
