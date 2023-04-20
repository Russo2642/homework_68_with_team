from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
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
            vacancies = vacancies.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(author__first_name__icontains=search, author__is_employer=True) |
                Q(profession__in=[item[0] for item in CategoryChoice.choices if search.lower() in item[1].lower()])
            )

        paginator = Paginator(vacancies, 5)
        page = request.GET.get('page')
        vacancies = paginator.get_page(page)

        context = {
            'vacancies': vacancies,
            'CategoryChoice': CategoryChoice.choices,
            'selected_category': category,
            'selected_sort': sort,
            'search_query': search,
        }
        return render(request, 'index.html', context=context)
