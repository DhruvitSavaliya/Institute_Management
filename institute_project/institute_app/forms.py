from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Student,Teacher,Department,Campus,Club,Parent,LibraryBook,Routine,Event

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','roll_no','department']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','email','subject']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = '__all__'

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = '__all__'

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'