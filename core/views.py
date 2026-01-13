
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Internship, Application

class HomeView(TemplateView):
    template_name = 'core/home.html'

class InternshipListView(ListView):
    model = Internship
    context_object_name = 'internships'
    template_name = 'core/internship_list.html'

class ApplicationCreateView(CreateView):
    model = Application
    fields = ['internship', 'full_name', 'email', 'portfolio_url', 'cover_letter']
    template_name = 'core/application_form.html'
    success_url = reverse_lazy('internship-list')

class ApplicationUpdateView(UpdateView):
    model = Application
    fields = ['full_name', 'email', 'portfolio_url', 'cover_letter']
    template_name = 'core/application_form.html'
    success_url = reverse_lazy('internship-list')
