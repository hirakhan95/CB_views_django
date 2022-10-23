from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher


# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYou(TemplateView):
    template_name = 'classroom/thankyou.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/form.html'

    success_url = '/classroom/thankyou/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thankyou')


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    queryset = Teacher.objects.order_by('first_name')


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # form --> confirm button
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')