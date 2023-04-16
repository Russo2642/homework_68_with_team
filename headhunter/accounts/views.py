from accounts.forms import CustomUserCreationForm
from accounts.forms import LoginForm
from accounts.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, 'Некорректные данные')
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Пользователь не найден')
            return redirect('login')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            user = get_user_model()
            data['html_book_list'] = render_to_string('user_details.html', {
                'user': user
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# class UserChangeView(UserPassesTestMixin, UpdateView):
#     model = get_user_model()
#     form_class = UserChangeForm
#     template_name = 'user_change.html'
#     context_object_name = 'user_obj'
#
#     def post(self, request, *args, **kwargs):
#         user = get_user_model()
#         form = UserChangeForm(request.POST, instance=user)
#         return save_book_form(request, form, self.template_name)
#
#     def get_success_url(self):
#         return reverse('profile', kwargs={'pk': self.object.pk})
#
#     def test_func(self):
#         return self.get_object() == self.request.user
def user_change_view(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
    else:
        form = UserChangeForm(instance=user)
    return save_book_form(request, form, 'user_change.html')
