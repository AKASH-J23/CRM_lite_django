from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Login',
    }

class CustomLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"

