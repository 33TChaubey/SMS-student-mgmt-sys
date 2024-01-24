from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Student
from django.urls import reverse_lazy
from student.forms import ItemForm


class ClassIndexView(ListView):
    model = Student
    context_object_name = 'StudentList'
    template_name = 'student/index.html'


class ClassDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'
    template_name = 'student/detail.html'


class UpdateDetailView(UpdateView):
    model = Student
    form_class = ItemForm
    template_name = 'student/item-form.html'
    success_url = '/student/index'
    
    def get_object(self, queryset=None):
        student_id = self.kwargs.get('student_id')
        return Student.objects.get(id=student_id)

class Additem(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student/item-form.html'
    success_url = reverse_lazy('student:index')
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user.username
        return super().form_valid(form)

class DeleteItemView(DeleteView):
    model = Student
    template_name = 'student/item-delete.html'
    success_url = reverse_lazy('student:index')
    
    
    def get_object(self, queryset=None):
        student_id = self.kwargs.get('student_id')
        return Student.objects.get(id=student_id)
    