from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from ..forms import RegisterForm

class UserRegisterView(CreateView):
    template_name = 'editor/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'editor/login.html'
    success_url = reverse_lazy('document_list')

    def get_success_url(self):
        # Check if there's a 'next' parameter in the URL
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('document_list')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')