def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    return {'login_form': form}

def include_signup_form(request):
    from .forms import NewUserForm
    form = NewUserForm()
    return {'signup_form': form}
