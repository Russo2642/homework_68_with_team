from accounts.forms import CustomUserCreationForm
from accounts.forms import LoginForm
from accounts.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
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


class ProfileView(UserPassesTestMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        kwargs["user_change_form"] = UserChangeForm(instance=self.request.user)
        return super().get_context_data(**kwargs)

    def test_func(self):
        return self.get_object() == self.request.user


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")

    def test_func(self):
        return self.get_object() == self.request.user
