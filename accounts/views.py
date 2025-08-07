from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import CustomUserForm

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Login',
    }

class CustomLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"

class customSignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = CustomUserForm
    success_url = reverse_lazy('auth:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return super().form_valid(form)
