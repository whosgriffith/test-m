from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import CustomUser
from .forms import CustomUserForm


class SignupView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('users_list')


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users_list.html'
    context_object_name = 'users'
