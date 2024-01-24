from django.urls import path, include
from student.models import Student
from student import views

app_name = 'student'

urlpatterns = [
    path('index/',views.ClassIndexView.as_view(),name='index'),
    path('detail/<int:student_id>/',views.ClassDetailView.as_view(),name='detail'),
    path('update/<int:student_id>/',views.UpdateDetailView.as_view(),name='update'),
    path('additem',views.Additem.as_view(),name='additem'),
    path('delete/<int:student_id>/',views.DeleteItemView.as_view(),name='delete')
]
