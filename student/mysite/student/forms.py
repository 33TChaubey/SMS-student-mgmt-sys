from student.models import Student
from django import forms
class ItemForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','Class','RollNo','Address','PhoneNo','DOB','Image']