from django.shortcuts import render
from django.views.generic import ListView
from .models import Cred


class Credential(ListView):
    template_name = 'personal_portfolio/credentials.html'
    model = Cred
    context_object_name = 'credential_data'
    paginate_by = 8